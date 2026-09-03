"""
SimplificationService — orchestrates the full AI pipeline.

Pipeline (fix C-1: all SLM calls run in thread pool executor):
  1. Resolve input text (from paste or document)
  2. Legal analysis — single multi-task SLM pass (fix H-1)
  3. RAG retrieval — per-domain collection (fix C-2)
  4. SLM↔Gemini routing — decision tree (fix H-3)
  5. Meaning validation
  6. Persist normalized results (3-table schema, fix H-2)
"""
import asyncio
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Any

import structlog
from sqlalchemy.ext.asyncio import AsyncSession

from models.session import SimplificationSession, SessionResult, SessionExtractedFact
from schemas.simplify import SimplifyRequest, SimplifyResponse

log = structlog.get_logger()

# Thread pool for CPU-bound SLM inference (fix C-1)
_slm_executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="slm-worker")


# ── SLM confidence threshold for routing decision (fix H-3) ──────────────────
SLM_CONFIDENCE_THRESHOLD = 0.75


class SimplificationService:

    @classmethod
    async def create_session(
        cls,
        db: AsyncSession,
        payload: SimplifyRequest,
        user_id: uuid.UUID | None,
    ) -> SimplificationSession:
        """Create a pending session and return immediately (async pattern)."""
        session = SimplificationSession(
            user_id=user_id,
            document_id=payload.document_id,
            input_text=payload.text,
            language=payload.language,
            legal_category=payload.legal_category,
            question=payload.question,
            status="pending",
        )
        db.add(session)
        await db.flush()
        return session

    @classmethod
    async def run_pipeline(
        cls,
        session_id: uuid.UUID,
        payload: SimplifyRequest,
        user_id: uuid.UUID | None,
    ) -> None:
        """
        Full async AI pipeline — runs after returning session_id to client.
        Call this as a background task: BackgroundTasks.add_task(run_pipeline, ...)
        """
        from database import AsyncSessionLocal
        from services.rag_service import RAGService
        from services.gemini_service import GeminiService
        from services.validation_service import ValidationService

        start = time.monotonic()

        async with AsyncSessionLocal() as db:
            try:
                # ── Step 1: Mark processing ─────────────────────────────────
                from sqlalchemy import select
                result = await db.execute(
                    select(SimplificationSession).where(SimplificationSession.id == session_id)
                )
                session = result.scalar_one()
                session.status = "processing"
                await db.flush()

                # ── Step 2: Resolve input text ───────────────────────────────
                input_text = await cls._resolve_input(payload)
                session.original_text = input_text

                # ── Step 3: Legal analysis (single SLM pass, fix H-1) ────────
                analysis = await cls._run_slm_analysis(input_text)

                # ── Step 4: RAG retrieval (per-domain, fix C-2) ──────────────
                rag_context, sources = [], []
                if payload.use_rag and payload.legal_category:
                    rag_context, sources = await RAGService.retrieve(
                        query=payload.question or input_text,
                        legal_category=payload.legal_category,
                        language=payload.language,
                    )

                # ── Step 5: SLM↔Gemini routing decision (fix H-3) ───────────
                simplified_text = ""
                gemini_used = False

                if analysis["confidence"] >= SLM_CONFIDENCE_THRESHOLD and not payload.use_gemini:
                    # High-confidence SLM result — skip Gemini
                    simplified_text = analysis["simplified_text"]
                    log.info("Using SLM output (high confidence)", confidence=analysis["confidence"])
                else:
                    # Use Gemini with RAG context
                    try:
                        simplified_text = await GeminiService.simplify(
                            original_text=input_text,
                            rag_context=rag_context,
                            language=payload.language,
                            legal_category=payload.legal_category,
                        )
                        gemini_used = True
                    except Exception as e:
                        # Fallback to SLM if Gemini fails (fix H-3: defined fallback)
                        log.warning("Gemini unavailable, falling back to SLM", error=str(e))
                        simplified_text = analysis.get("simplified_text", input_text)
                        session.error_code = "GEMINI_FALLBACK"

                # ── Step 6: Meaning validation ────────────────────────────────
                validation = await ValidationService.validate(input_text, simplified_text, analysis)
                meaning_score = validation["meaning_score"]

                # ── Step 7: Persist (normalized 3-table schema, fix H-2) ──────
                elapsed_ms = int((time.monotonic() - start) * 1000)

                session_result = SessionResult(
                    session_id=session_id,
                    simplified_text=simplified_text,
                    meaning_score=meaning_score,
                    processing_time_ms=elapsed_ms,
                    slm_used=True,
                    rag_used=bool(rag_context),
                    gemini_used=gemini_used,
                )
                db.add(session_result)

                # Store each extracted fact as a separate row (fix H-2)
                for fact_type, facts in [
                    ("entity", analysis.get("entities", [])),
                    ("condition", analysis.get("conditions", [])),
                    ("obligation", analysis.get("obligations", [])),
                    ("exception", analysis.get("exceptions", [])),
                    ("clause_type", [{"value": ct} for ct in analysis.get("clause_types", [])]),
                ]:
                    for fact in facts:
                        db.add(SessionExtractedFact(
                            session_id=session_id,
                            fact_type=fact_type,
                            fact_value=fact if isinstance(fact, dict) else {"value": fact},
                        ))

                session.status = "done"
                await db.commit()

                log.info("Pipeline complete", session_id=str(session_id), ms=elapsed_ms)

            except Exception as e:
                log.error("Pipeline failed", session_id=str(session_id), error=str(e))
                session.status = "error"
                session.error_message = str(e)
                session.error_code = "INTERNAL_ERROR"
                await db.commit()

    @classmethod
    async def _resolve_input(cls, payload: SimplifyRequest) -> str:
        """Resolve the input text from either pasted text or an uploaded document."""
        if payload.input_type == "text" and payload.text:
            return payload.text

        if payload.input_type == "document" and payload.document_id:
            from services.document_service import DocumentService
            return await DocumentService.get_extracted_text(payload.document_id)

        raise ValueError("No valid input provided")

    @classmethod
    async def _run_slm_analysis(cls, text: str) -> dict[str, Any]:
        """
        Run the SLM in a thread pool executor (fix C-1).
        Single multi-task forward pass returns all analysis at once (fix H-1).
        """
        loop = asyncio.get_event_loop()

        def _slm_inference(text: str) -> dict[str, Any]:
            """Blocking SLM inference — runs in thread pool."""
            # TODO: Replace with actual SLM model call once trained
            # from model.inference import SLMInference
            # return SLMInference.analyze_all(text)

            # Stub response for scaffold:
            return {
                "clause_types": ["OBLIGATION"],
                "entities": [{"text": "අයදුම්කරු", "type": "PERSON_ROLE"}],
                "conditions": [],
                "obligations": ["Submit application within deadline"],
                "exceptions": [],
                "simplified_text": text,  # Identity — replace with real model
                "confidence": 0.5,        # Low confidence → will route to Gemini
            }

        return await loop.run_in_executor(_slm_executor, _slm_inference, text)
