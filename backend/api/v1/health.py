"""
Health check endpoints.
GET /health         — Liveness (is the process running?)
GET /health/ready   — Readiness (are all dependencies up?)
"""
from typing import Any

import redis.asyncio as aioredis
from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from database import AsyncSessionLocal

router = APIRouter()


async def _check_database() -> str:
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
        return "ok"
    except Exception as e:
        return f"error: {e}"


async def _check_redis() -> str:
    try:
        r = aioredis.from_url(settings.REDIS_URL)
        await r.ping()
        await r.aclose()
        return "ok"
    except Exception as e:
        return f"error: {e}"


async def _check_chromadb() -> str:
    try:
        import httpx
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"http://{settings.CHROMA_HOST}:{settings.CHROMA_PORT}/api/v1/heartbeat",
                timeout=3.0,
            )
            return "ok" if resp.status_code == 200 else f"status {resp.status_code}"
    except Exception as e:
        return f"error: {e}"


@router.get("", summary="Liveness check")
async def health_live() -> dict[str, str]:
    """Returns 200 if the process is running."""
    return {"status": "alive", "version": settings.APP_VERSION}


@router.get("/ready", summary="Readiness check")
async def health_ready() -> dict[str, Any]:
    """Checks all downstream dependencies. Returns 200 if all are healthy."""
    checks = {
        "database": await _check_database(),
        "redis": await _check_redis(),
        "vector_store": await _check_chromadb(),
    }
    all_ok = all(v == "ok" for v in checks.values())
    return {
        "status": "ready" if all_ok else "degraded",
        "version": settings.APP_VERSION,
        "checks": checks,
    }
