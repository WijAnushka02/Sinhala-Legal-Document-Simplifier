"""
Simplification API endpoint.

POST /simplify          — Submit a simplification request (returns session_id immediately)
GET  /simplify/{id}     — Poll for / fetch completed result
"""
import uuid
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from dependencies import DbSession, get_current_user_optional, rate_limit_simplify
from models.session import SimplificationSession, SessionResult, SessionExtractedFact
from schemas.simplify import SimplifyRequest, SimplifyResponse, ExtractedEntity, SourceReference
from services.simplification_service import SimplificationService

router = APIRouter()


@router.post("", response_model=SimplifyResponse, status_code=status.HTTP_202_ACCEPTED)
async def create_simplification(
    payload: SimplifyRequest,
    background_tasks: BackgroundTasks,
    db: DbSession,
    _rate: Annotated[None, Depends(rate_limit_simplify)],
    current_user=Depends(get_current_user_optional),
) -> SimplifyResponse:
    """
    Submit text or a document for legal simplification.
    Returns a session_id immediately with status='pending'.
    Poll GET /simplify/{session_id} for the completed result.
    """
    user_id = current_user.id if current_user else None

    # Create pending session
    session = await SimplificationService.create_session(db, payload, user_id)
    await db.commit()

    # Run AI pipeline as a background task (fix C-1: non-blocking)
    background_tasks.add_task(
        SimplificationService.run_pipeline,
        session_id=session.id,
        payload=payload,
        user_id=user_id,
    )

    return SimplifyResponse(
        session_id=session.id,
        status="pending",
        created_at=session.created_at,
    )


@router.get("/{session_id}", response_model=SimplifyResponse)
async def get_simplification(
    session_id: uuid.UUID,
    db: DbSession,
    current_user=Depends(get_current_user_optional),
) -> SimplifyResponse:
    """
    Fetch the result of a simplification session.
    Returns status='pending' | 'processing' | 'done' | 'error'.
    """
    result = await db.execute(
        select(SimplificationSession)
        .where(SimplificationSession.id == session_id)
        .options(
            selectinload(SimplificationSession.result),
            selectinload(SimplificationSession.extracted_facts),
            selectinload(SimplificationSession.sources),
        )
    )
    session = result.scalar_one_or_none()

    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    # Authorization: allow owner or anonymous access if no user_id
    if session.user_id and current_user and session.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    return _build_response(session)


def _build_response(session: SimplificationSession) -> SimplifyResponse:
    """Build the API response from the normalized DB tables."""
    sr = session.result
    facts = session.extracted_facts or []

    entities = [
        ExtractedEntity(**f.fact_value)
        for f in facts if f.fact_type == "entity"
    ]
    conditions = [f.fact_value.get("value", "") for f in facts if f.fact_type == "condition"]
    obligations = [f.fact_value.get("value", "") for f in facts if f.fact_type == "obligation"]
    exceptions = [f.fact_value.get("value", "") for f in facts if f.fact_type == "exception"]
    clause_types = [f.fact_value.get("value", "") for f in facts if f.fact_type == "clause_type"]

    sources = []
    for ss in (session.sources or []):
        if ss.source:
            sources.append(SourceReference(
                source_id=ss.source_id,
                title=ss.source.title,
                relevance_score=ss.relevance_score or 0.0,
                url=ss.source.source_url,
            ))

    return SimplifyResponse(
        session_id=session.id,
        status=session.status,
        original_text=session.original_text,
        simplified_text=sr.simplified_text if sr else None,
        clause_types=clause_types,
        entities=entities,
        conditions=conditions,
        obligations=obligations,
        exceptions=exceptions,
        meaning_score=sr.meaning_score if sr else None,
        sources=sources,
        processing_time_ms=sr.processing_time_ms if sr else None,
        slm_used=sr.slm_used if sr else False,
        rag_used=sr.rag_used if sr else False,
        gemini_used=sr.gemini_used if sr else False,
        error_message=session.error_message,
        created_at=session.created_at,
    )
