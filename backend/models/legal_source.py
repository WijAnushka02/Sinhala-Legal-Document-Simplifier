"""
LegalSource and LegalChunk ORM models — the verified legal knowledge base.
"""
import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class LegalSource(Base):
    """A verified legal document (Act, Regulation, Gazette, etc.)"""
    __tablename__ = "legal_sources"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(Text, nullable=False)
    source_type: Mapped[str | None] = mapped_column(String(100))  # act|regulation|gazette|notice
    legal_category: Mapped[str | None] = mapped_column(String(100), index=True)
    language: Mapped[str] = mapped_column(String(10), default="si")
    publication_date: Mapped[date | None] = mapped_column(Date)
    last_verified: Mapped[date | None] = mapped_column(Date)
    updated_at: Mapped[datetime] = mapped_column(    # Fix L-3: add updated_at
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    source_url: Mapped[str | None] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # Relationships
    chunks: Mapped[list["LegalChunk"]] = relationship(
        back_populates="source", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<LegalSource id={self.id} title={self.title[:40]}>"


class LegalChunk(Base):
    """A chunked segment of a LegalSource, embedded and stored in ChromaDB."""
    __tablename__ = "legal_chunks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("legal_sources.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    chunk_text: Mapped[str] = mapped_column(Text, nullable=False)
    clause_type: Mapped[str | None] = mapped_column(String(100))   # OBLIGATION|RIGHT|CONDITION…
    chroma_doc_id: Mapped[str | None] = mapped_column(String, index=True)  # ID in ChromaDB
    updated_at: Mapped[datetime] = mapped_column(    # Fix L-3
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # Relationships
    source: Mapped["LegalSource"] = relationship(back_populates="chunks")

    def __repr__(self) -> str:
        return f"<LegalChunk id={self.id} source_id={self.source_id} index={self.chunk_index}>"
