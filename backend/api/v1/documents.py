"""Stub routes for documents, history, query, api-keys."""
# ── documents.py ──────────────────────────────────────────────────────────────
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from dependencies import DbSession, get_current_user, rate_limit_upload
from typing import Annotated
import uuid

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_202_ACCEPTED)
async def upload_document(
    file: UploadFile = File(...),
    language: str = "si",
    legal_category: str | None = None,
    db: DbSession = Depends(),
    _rate: Annotated[None, Depends(rate_limit_upload)] = None,
    current_user=Depends(get_current_user),
):
    """Upload a PDF or DOCX legal document for processing."""
    from services.document_service import DocumentService
    doc = await DocumentService.upload(db, file, current_user.id, language, legal_category)
    await db.commit()
    return {"id": doc.id, "filename": doc.filename, "status": doc.status}


@router.get("")
async def list_documents(db: DbSession = Depends(), current_user=Depends(get_current_user)):
    from sqlalchemy import select
    from models.document import UploadedDocument
    result = await db.execute(
        select(UploadedDocument)
        .where(UploadedDocument.user_id == current_user.id)
        .order_by(UploadedDocument.created_at.desc())
        .limit(50)
    )
    docs = result.scalars().all()
    return [{"id": d.id, "filename": d.filename, "status": d.status, "created_at": d.created_at} for d in docs]


@router.get("/{doc_id}")
async def get_document(doc_id: uuid.UUID, db: DbSession = Depends(), current_user=Depends(get_current_user)):
    from sqlalchemy import select
    from models.document import UploadedDocument
    result = await db.execute(select(UploadedDocument).where(UploadedDocument.id == doc_id))
    doc = result.scalar_one_or_none()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    if doc.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")
    return doc


@router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(doc_id: uuid.UUID, db: DbSession = Depends(), current_user=Depends(get_current_user)):
    from sqlalchemy import select, delete
    from models.document import UploadedDocument
    result = await db.execute(select(UploadedDocument).where(UploadedDocument.id == doc_id))
    doc = result.scalar_one_or_none()
    if not doc or doc.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Document not found")
    await db.delete(doc)
