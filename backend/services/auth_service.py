"""
AuthService — password hashing, JWT creation, user lookup.
"""
import hashlib
import secrets
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from models.user import User
from models.api_key import ApiKey
from schemas.auth import RegisterRequest, LoginRequest
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    # ── Password ────────────────────────────────────────────────────────────
    @staticmethod
    def hash_password(plain: str) -> str:
        return pwd_context.hash(plain)

    @staticmethod
    def verify_password(plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)

    # ── JWT ─────────────────────────────────────────────────────────────────
    @staticmethod
    def _create_token(data: dict[str, Any], expire_delta: timedelta) -> str:
        payload = data.copy()
        payload["exp"] = datetime.now(timezone.utc) + expire_delta
        return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    @classmethod
    def create_access_token(cls, user_id: uuid.UUID) -> str:
        return cls._create_token(
            {"sub": str(user_id), "type": "access"},
            timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
        )

    @classmethod
    def create_refresh_token(cls, user_id: uuid.UUID) -> str:
        return cls._create_token(
            {"sub": str(user_id), "type": "refresh"},
            timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS),
        )

    # ── Register / Login ────────────────────────────────────────────────────
    @classmethod
    async def register(cls, db: AsyncSession, payload: RegisterRequest) -> User:
        existing = await db.execute(select(User).where(User.email == payload.email))
        if existing.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
        user = User(
            email=payload.email,
            password_hash=cls.hash_password(payload.password),
            display_name=payload.display_name,
        )
        db.add(user)
        await db.flush()
        return user

    @classmethod
    async def login(cls, db: AsyncSession, payload: LoginRequest) -> dict[str, Any]:
        result = await db.execute(select(User).where(User.email == payload.email))
        user = result.scalar_one_or_none()

        if not user or not cls.verify_password(payload.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is disabled",
            )

        return {
            "access_token": cls.create_access_token(user.id),
            "refresh_token": cls.create_refresh_token(user.id),
            "expires_in": settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        }

    @classmethod
    async def refresh(cls, db: AsyncSession, refresh_token: str) -> dict[str, Any]:
        try:
            payload = jwt.decode(
                refresh_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
            )
            if payload.get("type") != "refresh":
                raise JWTError("Wrong token type")
            user_id = uuid.UUID(payload["sub"])
        except (JWTError, ValueError):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired refresh token",
            )

        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user or not user.is_active:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

        return {
            "access_token": cls.create_access_token(user.id),
            "refresh_token": cls.create_refresh_token(user.id),
            "expires_in": settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        }

    # ── Resolve user from JWT ────────────────────────────────────────────────
    @classmethod
    async def get_user_from_jwt(cls, db: AsyncSession, token: str) -> User | None:
        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
            )
            if payload.get("type") != "access":
                return None
            user_id = uuid.UUID(payload["sub"])
        except (JWTError, ValueError):
            return None

        result = await db.execute(select(User).where(User.id == user_id, User.is_active == True))
        return result.scalar_one_or_none()

    # ── Resolve user from API key ────────────────────────────────────────────
    @classmethod
    async def get_user_from_api_key(cls, db: AsyncSession, raw_key: str) -> User | None:
        key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
        result = await db.execute(
            select(ApiKey).where(ApiKey.key_hash == key_hash)
        )
        api_key = result.scalar_one_or_none()
        if not api_key:
            return None

        # Check expiry
        if api_key.expires_at and api_key.expires_at < datetime.now(timezone.utc):
            return None

        # Update last_used (fire-and-forget — don't block request)
        api_key.last_used = datetime.now(timezone.utc)

        user_result = await db.execute(
            select(User).where(User.id == api_key.user_id, User.is_active == True)
        )
        return user_result.scalar_one_or_none()
