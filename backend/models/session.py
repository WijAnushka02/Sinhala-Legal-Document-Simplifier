"""
Simplification session ORM models — 3 normalized tables (fixes H-2).

  SimplificationSession  — immutable input context + status
  SessionResult          — AI output, written once when processing is done
  SessionExtractedFact   — one row per extracted legal fact (extensible)
"""
import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, SmallInteger, String, Text, func
from sqlalchemy import JSON as JSONB, Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# ──────────────────────────────────────────────────────────────────────────────
# Table 1 — Core session (immutable input + lifecycle)
# ──────────────────────────────────────────────────────────────────────────────
class SimplificationSession(Base):
    __tablename__ = "simplification_sessions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), index=True
    )
    document_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("uploaded_documents.id", ondelete="SET NULL")
    )
    input_text: Mapped[str | None] = mapped_column(Text)            # Pasted text input
    original_text: Mapped[str | None] = mapped_column(Text)         # Exact text processed
    language: Mapped[str] = mapped_column(String(10), default="si")
    legal_category: Mapped[str | None] = mapped_column(String(100))
    question: Mapped[str | None] = mapped_column(Text)              # Optional user question
    status: Mapped[str] = mapped_column(String(50), default="pending", index=True)
    error_message: Mapped[str | None] = mapped_column(Text)
    error_code: Mapped[str | None] = mapped_column(String(50))      # Fix L-4: structured errors
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="sessions")
    document: Mapped["UploadedDocument"] = relationship(back_populates="sessions")
    result: Mapped["SessionResult | None"] = relationship(back_populates="session", uselist=False)
    extracted_facts: Mapped[list["SessionExtractedFact"]] = relationship(
        back_populates="session", cascade="all, delete-orphan"
    )
    sources: Mapped[list["SessionSource"]] = relationship(
        back_populates="session", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<SimplificationSession id={self.id} status={self.status}>"


# ──────────────────────────────────────────────────────────────────────────────
# Table 2 — AI output (written once when done)
# ──────────────────────────────────────────────────────────────────────────────
class SessionResult(Base):
    __tablename__ = "session_results"

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("simplification_sessions.id", ondelete="CASCADE"),
        primary_key=True,
    )
    simplified_text: Mapped[str | None] = mapped_column(Text)
    meaning_score: Mapped[float | None] = mapped_column(Float)      # 0.0 – 1.0
    processing_time_ms: Mapped[int | None] = mapped_column(Integer)
    slm_used: Mapped[bool] = mapped_column(Boolean, default=False)
    rag_used: Mapped[bool] = mapped_column(Boolean, default=False)
    gemini_used: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # Relationships
    session: Mapped["SimplificationSession"] = relationship(back_populates="result")


# ──────────────────────────────────────────────────────────────────────────────
# Table 3 — Extracted legal facts (one row per fact, fully extensible)
# ──────────────────────────────────────────────────────────────────────────────
class SessionExtractedFact(Base):
    __tablename__ = "session_extracted_facts"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("simplification_sessions.id", ondelete="CASCADE"),
        index=True,
    )
    # fact_type: 'entity' | 'condition' | 'obligation' | 'exception' | 'date' | 'number' | 'clause_type'
    fact_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    fact_value: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False)
    preserved: Mapped[bool | None] = mapped_column(Boolean)         # Was this fact in simplified text?

    # Relationships
    session: Mapped["SimplificationSession"] = relationship(back_populates="extracted_facts")

    def __repr__(self) -> str:
        return f"<SessionExtractedFact type={self.fact_type}>"


# ──────────────────────────────────────────────────────────────────────────────
# Table 4 — RAG sources used in this session
# ──────────────────────────────────────────────────────────────────────────────
class SessionSource(Base):
    __tablename__ = "session_sources"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("simplification_sessions.id", ondelete="CASCADE"),
        index=True,
    )
    source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("legal_sources.id"), nullable=False
    )
    chunk_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("legal_chunks.id")
    )
    relevance_score: Mapped[float | None] = mapped_column(Float)
    rank: Mapped[int | None] = mapped_column(SmallInteger)

    # Relationships
    session: Mapped["SimplificationSession"] = relationship(back_populates="sources")
    source: Mapped["LegalSource"] = relationship()
    chunk: Mapped["LegalChunk | None"] = relationship()
