"""Pydantic v2 schemas for authentication endpoints."""
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    display_name: str | None = Field(None, max_length=100)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds


class UserResponse(BaseModel):
    id: UUID
    email: str
    display_name: str | None
    preferred_lang: str
    created_at: datetime

    model_config = {"from_attributes": True}


class ApiKeyCreateRequest(BaseModel):
    name: str = Field(max_length=100)


class ApiKeyResponse(BaseModel):
    id: UUID
    name: str | None
    created_at: datetime
    expires_at: datetime | None

    model_config = {"from_attributes": True}


class ApiKeyCreatedResponse(ApiKeyResponse):
    """Returned ONCE on creation — includes the raw key."""
    raw_key: str
