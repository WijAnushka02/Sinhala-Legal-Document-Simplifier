"""Pydantic v2 schemas for simplification endpoints."""
from uuid import UUID
from datetime import datetime
from typing import Any, Literal
from pydantic import BaseModel, Field


class SimplifyRequest(BaseModel):
    input_type: Literal["text", "document"]
    text: str | None = Field(None, min_length=10, max_length=50_000)
    document_id: UUID | None = None
    language: Literal["si", "ta", "en"] = "si"
    legal_category: str | None = None
    question: str | None = Field(None, max_length=500)
    use_rag: bool = True
    use_gemini: bool = True


class ExtractedEntity(BaseModel):
    text: str
    type: str  # PERSON_ROLE | ORGANIZATION | DATE | NUMBER | LOCATION | LAW


class SourceReference(BaseModel):
    source_id: UUID
    title: str
    section: str | None = None
    relevance_score: float
    url: str | None = None


class SimplifyResponse(BaseModel):
    session_id: UUID
    status: str
    original_text: str | None = None
    simplified_text: str | None = None
    clause_types: list[str] = []
    entities: list[ExtractedEntity] = []
    conditions: list[str] = []
    obligations: list[str] = []
    exceptions: list[str] = []
    dates: list[dict[str, Any]] = []
    numbers: list[dict[str, Any]] = []
    meaning_score: float | None = None
    sources: list[SourceReference] = []
    processing_time_ms: int | None = None
    slm_used: bool = False
    rag_used: bool = False
    gemini_used: bool = False
    error_message: str | None = None
    created_at: datetime | None = None

    model_config = {"from_attributes": True}


class QueryRequest(BaseModel):
    question: str = Field(min_length=5, max_length=500)
    language: Literal["si", "ta", "en"] = "si"
    legal_category: str | None = None
    session_id: UUID | None = None  # Optional: provide document context


class QueryResponse(BaseModel):
    session_id: UUID
    answer: str
    sources: list[SourceReference] = []
    confidence: float | None = None
    processing_time_ms: int | None = None
