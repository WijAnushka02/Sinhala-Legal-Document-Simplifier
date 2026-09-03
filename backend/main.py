"""
Sinhala Legal Document Simplifier — FastAPI Application Entry Point
"""
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from config import settings
from database import init_db
from api.v1.router import router as api_v1_router

log = structlog.get_logger()


# ──────────────────────────────────────────────────────────────────────────────
# Lifespan — startup / shutdown logic
# ──────────────────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle application startup and shutdown."""
    log.info("Starting Sinhala Legal Document Simplifier API", version=settings.APP_VERSION)

    # Initialize database (create tables if they don't exist)
    await init_db()

    # Ensure upload directory exists
    import os
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    log.info("Application startup complete")
    yield  # ← Application runs here

    log.info("Application shutting down")


# ──────────────────────────────────────────────────────────────────────────────
# App instance
# ──────────────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="Sinhala Legal Document Simplifier API",
    description=(
        "AI-powered simplification of Sri Lankan legal documents using "
        "a Sinhala Small Language Model, RAG, and the Gemini API."
    ),
    version=settings.APP_VERSION,
    docs_url="/docs" if settings.APP_DEBUG else None,
    redoc_url="/redoc" if settings.APP_DEBUG else None,
    lifespan=lifespan,
)


# ──────────────────────────────────────────────────────────────────────────────
# Middleware
# ──────────────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS_LIST,
    allow_credentials=True,          # Required for HttpOnly cookie (refresh token)
    allow_methods=["*"],
    allow_headers=["*"],
)

if not settings.APP_DEBUG:
    # Block requests from unexpected hosts in production
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"],         # Override in production with your actual domain
    )


# ──────────────────────────────────────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────────────────────────────────────
app.include_router(api_v1_router, prefix="/api/v1")
