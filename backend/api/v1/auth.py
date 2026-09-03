"""
Authentication endpoints.
POST /auth/register   — Create user account
POST /auth/login      — Get access token (+ HttpOnly refresh cookie)
POST /auth/refresh    — Rotate access token using refresh cookie
POST /auth/logout     — Invalidate refresh token
GET  /auth/me         — Get current user profile
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import DbSession, get_current_user
from schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from services.auth_service import AuthService

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest, db: DbSession) -> UserResponse:
    """Create a new user account."""
    user = await AuthService.register(db, payload)
    return UserResponse.model_validate(user)


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, response: Response, db: DbSession) -> TokenResponse:
    """Authenticate and receive JWT tokens. Refresh token is set as HttpOnly cookie."""
    result = await AuthService.login(db, payload)

    # Set refresh token as HttpOnly cookie (not accessible to JavaScript)
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=True,      # HTTPS only in production
        samesite="lax",
        max_age=60 * 60 * 24 * 30,  # 30 days
        path="/api/v1/auth/refresh",
    )

    return TokenResponse(
        access_token=result["access_token"],
        expires_in=result["expires_in"],
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    response: Response,
    db: DbSession,
    refresh_token: str | None = None,  # From HttpOnly cookie
) -> TokenResponse:
    """Rotate the access token using the refresh token cookie."""
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token missing",
        )
    result = await AuthService.refresh(db, refresh_token)

    # Rotate refresh token
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 30,
        path="/api/v1/auth/refresh",
    )
    return TokenResponse(
        access_token=result["access_token"],
        expires_in=result["expires_in"],
    )


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response, current_user=Depends(get_current_user)) -> None:
    """Invalidate the refresh token cookie."""
    response.delete_cookie(key="refresh_token", path="/api/v1/auth/refresh")


@router.get("/me", response_model=UserResponse)
async def get_me(current_user=Depends(get_current_user)) -> UserResponse:
    """Get the authenticated user's profile."""
    return UserResponse.model_validate(current_user)
