"""
Application configuration — reads from environment variables / .env file.
All settings are validated by Pydantic at startup.
"""
from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ── Application ─────────────────────────────────────────
    APP_ENV: str = "development"
    APP_SECRET_KEY: str
    APP_DEBUG: bool = True
    APP_VERSION: str = "1.0.0"

    # ── Server ───────────────────────────────────────────────
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000
    ALLOWED_ORIGINS: str = "http://localhost:5173"

    @property
    def ALLOWED_ORIGINS_LIST(self) -> List[str]:
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",")]

    # ── Database ─────────────────────────────────────────────
    DATABASE_URL: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "sinhala_legal_db"
    POSTGRES_USER: str = "legal_user"
    POSTGRES_PASSWORD: str

    # ── ChromaDB ─────────────────────────────────────────────
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8001
    CHROMA_COLLECTION_PREFIX: str = "legal_"  # Per-domain: legal_consumer_law, etc.

    # ── Redis ────────────────────────────────────────────────
    REDIS_URL: str = "redis://localhost:6379/0"

    # ── Gemini ───────────────────────────────────────────────
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-1.5-pro"

    # ── JWT ──────────────────────────────────────────────────
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # ── Rate limiting ────────────────────────────────────────
    RATE_LIMIT_SIMPLIFY_PER_MINUTE: int = 10
    RATE_LIMIT_QUERY_PER_MINUTE: int = 20
    RATE_LIMIT_UPLOAD_PER_MINUTE: int = 5
    RATE_LIMIT_DEFAULT_PER_MINUTE: int = 100

    # ── File storage ─────────────────────────────────────────
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE_MB: int = 10
    ALLOWED_MIME_TYPES: str = (
        "application/pdf,"
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    @property
    def ALLOWED_MIME_TYPES_LIST(self) -> List[str]:
        return [m.strip() for m in self.ALLOWED_MIME_TYPES.split(",")]

    @property
    def MAX_UPLOAD_SIZE_BYTES(self) -> int:
        return self.MAX_UPLOAD_SIZE_MB * 1024 * 1024

    # ── ML model ─────────────────────────────────────────────
    SLM_MODEL_PATH: str = "./training/checkpoints/best_model.pt"
    SLM_MAX_LENGTH: int = 512
    EMBEDDING_MODEL: str = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

    # ── Logging ──────────────────────────────────────────────
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "production"


@lru_cache
def get_settings() -> Settings:
    """Cached singleton — reads .env once at startup."""
    return Settings()


# Module-level singleton for easy import
settings: Settings = get_settings()
