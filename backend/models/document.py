"""
UploadedDocument ORM model.
Note: extracted_text is NOT stored in the DB (scalability risk M-2).
Instead, extracted_text_path points to the file on disk/S3.
"""
import uuid
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, func
from sqlalchemy import Uuid as UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class UploadedDocument(Base):
    __tablename__ = "uploaded_documents"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), index=True
    )
    filename: Mapped[str] = mapped_column(String, nullable=False)
    file_path: Mapped[str] = mapped_column(String, nullable=False)          # Original file path
    extracted_text_path: Mapped[str | None] = mapped_column(String)         # Fix M-2: path not content
    mime_type: Mapped[str | None] = mapped_column(String(100))
    file_size_bytes: Mapped[int | None] = mapped_column(BigInteger)
    language: Mapped[str] = mapped_column(String(10), default="si")
    legal_category: Mapped[str | None] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(50), default="pending")      # pending|processing|ready|failed
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="documents")
    sessions: Mapped[list["SimplificationSession"]] = relationship(back_populates="document")

    def __repr__(self) -> str:
        return f"<UploadedDocument id={self.id} filename={self.filename} status={self.status}>"
