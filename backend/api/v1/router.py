"""API v1 router — aggregates all route modules."""
from fastapi import APIRouter

from api.v1 import health, auth, documents, simplify, query, history, api_keys

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["Health"])
router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(documents.router, prefix="/documents", tags=["Documents"])
router.include_router(simplify.router, prefix="/simplify", tags=["Simplification"])
router.include_router(query.router, prefix="/query", tags=["Query"])
router.include_router(history.router, prefix="/history", tags=["History"])
router.include_router(api_keys.router, prefix="/api-keys", tags=["API Keys"])
