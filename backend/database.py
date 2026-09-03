"""
Database — async SQLAlchemy engine and session factory.
Uses asyncpg driver for non-blocking I/O with FastAPI.
"""
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from config import settings

# ──────────────────────────────────────────────────────────────────────────────
# Engine
# ──────────────────────────────────────────────────────────────────────────────
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.APP_DEBUG,          # Log SQL queries in debug mode
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,               # Verify connections before use
)

# ──────────────────────────────────────────────────────────────────────────────
# Session factory
# ──────────────────────────────────────────────────────────────────────────────
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,           # Keep objects usable after commit
)


# ──────────────────────────────────────────────────────────────────────────────
# Base class for all ORM models
# ──────────────────────────────────────────────────────────────────────────────
class Base(DeclarativeBase):
    pass


# ──────────────────────────────────────────────────────────────────────────────
# Async generator for dependency injection
# ──────────────────────────────────────────────────────────────────────────────
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency — yields an async database session per request.
    Rolls back on exception, always closes session.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


# ──────────────────────────────────────────────────────────────────────────────
# Init — called at application startup
# ──────────────────────────────────────────────────────────────────────────────
async def init_db() -> None:
    """
    Create all tables if they do not exist.
    In production, prefer Alembic migrations over this.
    """
    # Import all models so SQLAlchemy knows about them
    from models import user, api_key, document, session, legal_source  # noqa: F401

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
