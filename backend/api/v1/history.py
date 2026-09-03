"""History, Query and API Key routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import uuid
from dependencies import DbSession, get_current_user
from models.session import SimplificationSession

router = APIRouter()

@router.get("")
async def list_history(
    page: int = 1, limit: int = 20, category: str | None = None,
    db: DbSession = Depends(), current_user=Depends(get_current_user),
):
    limit = min(limit, 100)
    q = select(SimplificationSession).where(SimplificationSession.user_id == current_user.id)
    if category:
        q = q.where(SimplificationSession.legal_category == category)
    q = q.order_by(SimplificationSession.created_at.desc()).offset((page - 1) * limit).limit(limit)
    result = await db.execute(q)
    sessions = result.scalars().all()
    return {
        "items": [
            {"session_id": s.id, "status": s.status, "legal_category": s.legal_category,
             "created_at": s.created_at}
            for s in sessions
        ],
        "page": page, "limit": limit,
    }


@router.get("/{session_id}")
async def get_history_item(session_id: uuid.UUID, db: DbSession = Depends(), current_user=Depends(get_current_user)):
    result = await db.execute(
        select(SimplificationSession)
        .where(SimplificationSession.id == session_id)
        .options(selectinload(SimplificationSession.result), selectinload(SimplificationSession.extracted_facts))
    )
    session = result.scalar_one_or_none()
    if not session or session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Session not found")
    from api.v1.simplify import _build_response
    return _build_response(session)


@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_history_item(session_id: uuid.UUID, db: DbSession = Depends(), current_user=Depends(get_current_user)):
    result = await db.execute(select(SimplificationSession).where(SimplificationSession.id == session_id))
    session = result.scalar_one_or_none()
    if not session or session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Session not found")
    await db.delete(session)
