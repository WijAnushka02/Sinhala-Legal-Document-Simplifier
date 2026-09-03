"""
DocumentService — file upload, storage, and text extraction coordination.
"""
import aiofiles
import os
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from models.document import UploadedDocument


class DocumentService:

    @classmethod
    async def upload(
        cls,
        db: AsyncSession,
        file: UploadFile,
        user_id: uuid.UUID,
        language: str = "si",
        legal_category: str | None = None,
    ) -> UploadedDocument:
        """Save uploaded file and create DB record. Text extraction runs as background task."""
        # Validate MIME type
        if file.content_type not in settings.ALLOWED_MIME_TYPES_LIST:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail=f"File type '{file.content_type}' not supported. Use PDF or DOCX.",
            )

        # Read and validate size
        content = await file.read()
        if len(content) > settings.MAX_UPLOAD_SIZE_BYTES:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail=f"File too large. Maximum size is {settings.MAX_UPLOAD_SIZE_MB} MB.",
            )

        # Save file to disk
        doc_id = uuid.uuid4()
        upload_dir = Path(settings.UPLOAD_DIR) / str(user_id)
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / f"{doc_id}_{file.filename}"

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(content)

        # Create DB record
        doc = UploadedDocument(
            id=doc_id,
            user_id=user_id,
            filename=file.filename,
            file_path=str(file_path),
            mime_type=file.content_type,
            file_size_bytes=len(content),
            language=language,
            legal_category=legal_category,
            status="processing",
        )
        db.add(doc)
        await db.flush()

        # TODO: Schedule text extraction as background task
        # background_tasks.add_task(cls._extract_text, doc.id, file_path, file.content_type)

        return doc

    @classmethod
    async def get_extracted_text(cls, document_id: uuid.UUID) -> str:
        """Read extracted text from the saved text file path."""
        from database import AsyncSessionLocal
        from sqlalchemy import select

        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(UploadedDocument).where(UploadedDocument.id == document_id)
            )
            doc = result.scalar_one_or_none()

        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        if doc.status != "ready":
            raise HTTPException(status_code=400, detail="Document not yet processed")
        if not doc.extracted_text_path:
            raise HTTPException(status_code=400, detail="No extracted text available")

        async with aiofiles.open(doc.extracted_text_path, "r", encoding="utf-8") as f:
            return await f.read()
