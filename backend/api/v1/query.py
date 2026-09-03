"""Query (RAG question-answering) endpoint."""
from typing import Annotated
from fastapi import APIRouter, Depends
from dependencies import DbSession, get_current_user_optional, rate_limit_query
from schemas.simplify import QueryRequest, QueryResponse
from services.rag_service import RAGService
from services.gemini_service import GeminiService
import uuid, time

router = APIRouter()

@router.post("", response_model=QueryResponse)
async def ask_legal_question(
    payload: QueryRequest,
    db: DbSession,
    _rate: Annotated[None, Depends(rate_limit_query)],
    current_user=Depends(get_current_user_optional),
) -> QueryResponse:
    """Ask a legal question grounded in the RAG knowledge base."""
    start = time.monotonic()

    rag_context, sources = [], []
    if payload.legal_category:
        rag_context, sources = await RAGService.retrieve(
            query=payload.question,
            legal_category=payload.legal_category,
            language=payload.language,
        )

    answer = await GeminiService.answer_query(
        question=payload.question,
        rag_context=rag_context,
        language=payload.language,
    )

    from schemas.simplify import SourceReference
    return QueryResponse(
        session_id=uuid.uuid4(),
        answer=answer,
        sources=[SourceReference(**s) for s in sources if s.get("source_id")],
        processing_time_ms=int((time.monotonic() - start) * 1000),
    )
