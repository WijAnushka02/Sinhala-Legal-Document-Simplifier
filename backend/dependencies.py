"""
FastAPI dependency injection functions.
Provides: database session, current user (JWT or API key), rate limiting.
"""
from typing import Annotated
from uuid import UUID

import redis.asyncio as aioredis
from fastapi import Cookie, Depends, Header, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from database import get_db

bearer_scheme = HTTPBearer(auto_error=False)

# ──────────────────────────────────────────────────────────────────────────────
# Redis connection pool
# ──────────────────────────────────────────────────────────────────────────────
_redis_pool: aioredis.Redis | None = None


async def get_redis() -> aioredis.Redis:
    """Lazy singleton Redis connection."""
    global _redis_pool
    if _redis_pool is None:
        _redis_pool = aioredis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
        )
    return _redis_pool


# ──────────────────────────────────────────────────────────────────────────────
# Current user — supports both JWT Bearer and X-API-Key
# ──────────────────────────────────────────────────────────────────────────────
async def get_current_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    bearer: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)] = None,
    x_api_key: Annotated[str | None, Header()] = None,
):
    """
    Resolves authenticated user from:
      1. Authorization: Bearer <jwt>
      2. X-API-Key: <raw_api_key>
    Raises 401 if neither is provided or invalid.
    """
    from services.auth_service import AuthService

    if bearer is not None:
        user = await AuthService.get_user_from_jwt(db, bearer.credentials)
        if user:
            return user

    if x_api_key is not None:
        user = await AuthService.get_user_from_api_key(db, x_api_key)
        if user:
            return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def get_current_user_optional(
    db: Annotated[AsyncSession, Depends(get_db)],
    bearer: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)] = None,
    x_api_key: Annotated[str | None, Header()] = None,
):
    """Like get_current_user but returns None instead of raising 401."""
    try:
        return await get_current_user(db, bearer, x_api_key)
    except HTTPException:
        return None


# ──────────────────────────────────────────────────────────────────────────────
# Rate limiting — Redis sliding window (NOT Oracle DB)
# ──────────────────────────────────────────────────────────────────────────────
async def _check_rate_limit(
    identifier: str,
    limit: int,
    window_seconds: int = 60,
    redis: aioredis.Redis = None,
) -> None:
    """
    Atomic Redis sliding window rate limiter.
    Raises HTTP 429 if limit exceeded.
    """
    if redis is None:
        return  # Skip rate limiting if Redis unavailable (dev mode)

    key = f"rl:{identifier}:{window_seconds}"
    pipe = redis.pipeline()
    pipe.incr(key)
    pipe.expire(key, window_seconds)
    results = await pipe.execute()
    count = results[0]

    if count > limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Try again in {window_seconds} seconds.",
            headers={"Retry-After": str(window_seconds)},
        )


def make_rate_limiter(limit_key: str, limit_attr: str):
    """Factory that creates a rate-limiting dependency for a specific endpoint."""

    async def _limiter(
        request: Request,
        redis: Annotated[aioredis.Redis, Depends(get_redis)],
        current_user=Depends(get_current_user_optional),
    ):
        identifier = (
            str(current_user.id) if current_user else request.client.host
        )
        limit = getattr(settings, limit_attr)
        await _check_rate_limit(identifier, limit, redis=redis)

    return _limiter


# Pre-built rate limiters for each endpoint group
rate_limit_simplify = make_rate_limiter("simplify", "RATE_LIMIT_SIMPLIFY_PER_MINUTE")
rate_limit_query = make_rate_limiter("query", "RATE_LIMIT_QUERY_PER_MINUTE")
rate_limit_upload = make_rate_limiter("upload", "RATE_LIMIT_UPLOAD_PER_MINUTE")

# Type aliases for readability
DbSession = Annotated[AsyncSession, Depends(get_db)]
