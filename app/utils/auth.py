from datetime import datetime, timedelta, timezone
import jwt
from typing import Optional
from app.config.settings import settings
from fastapi import HTTPException, status, Depends
from app.constants.message import Messages
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# FastAPI HTTPBearer instance to extract token from Authorization header
bearer_scheme = HTTPBearer()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generates a JWT access token using UTC-aware datetime.
    """
    to_encode = data.copy()
    expire = datetime.now(
        timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.jwt.SECRET_KEY,
                       algorithm=settings.jwt.ALGORITHM)
    return token


def get_authenticate(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> dict:
    """
    Dependency to get the current logged-in user from JWT Bearer token.
    Raises 401 if token is missing, invalid, or expired.
    """
    token = credentials.credentials
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=Messages.INVALID_TOKEN
        )

    try:
        payload = jwt.decode(token, settings.jwt.SECRET_KEY,
                             algorithms=[settings.jwt.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=Messages.TOKEN_EXPIRED)
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=Messages.INVALID_TOKEN)
    except HTTPException as e:
        raise e
