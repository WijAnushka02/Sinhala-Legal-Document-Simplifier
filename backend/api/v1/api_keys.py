"""API key management endpoints."""
import hashlib, secrets
from fastapi import APIRouter, Depends, status
from dependencies import DbSession, get_current_user
from models.api_key import ApiKey
from schemas.auth import ApiKeyCreateRequest, ApiKeyCreatedResponse, ApiKeyResponse
from sqlalchemy import select
import uuid

router = APIRouter()

@router.post("", response_model=ApiKeyCreatedResponse, status_code=status.HTTP_201_CREATED)
async def create_api_key(payload: ApiKeyCreateRequest, db: DbSession = Depends(), current_user=Depends(get_current_user)):
    raw_key = f"slm_{secrets.token_urlsafe(32)}"
    key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
    api_key = ApiKey(user_id=current_user.id, key_hash=key_hash, name=payload.name)
    db.add(api_key)
    await db.flush()
    return ApiKeyCreatedResponse(id=api_key.id, name=api_key.name, created_at=api_key.created_at, expires_at=api_key.expires_at, raw_key=raw_key)

@router.get("", response_model=list[ApiKeyResponse])
async def list_api_keys(db: DbSession = Depends(), current_user=Depends(get_current_user)):
    result = await db.execute(select(ApiKey).where(ApiKey.user_id == current_user.id))
    return [ApiKeyResponse.model_validate(k) for k in result.scalars().all()]

@router.delete("/{key_id}", status_code=status.HTTP_204_NO_CONTENT)
async def revoke_api_key(key_id: uuid.UUID, db: DbSession = Depends(), current_user=Depends(get_current_user)):
    result = await db.execute(select(ApiKey).where(ApiKey.id == key_id, ApiKey.user_id == current_user.id))
    key = result.scalar_one_or_none()
    if key:
        await db.delete(key)
