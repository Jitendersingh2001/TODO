from datetime import datetime, timedelta, timezone
import jwt
from typing import Optional
from app.config.settings import settings
from fastapi import HTTPException, status
from app.constants.message import Messages

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generates a JWT access token using UTC-aware datetime.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.jwt.SECRET_KEY, algorithm=settings.jwt.ALGORITHM)
    return token


def decode_access_token(token: str) -> dict:
    """
    Decodes and validates a JWT access token.
    """
    try:
        payload = jwt.decode(token, settings.jwt.SECRET_KEY, algorithms=[settings.jwt.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=Messages.TOKEN_EXPIRED)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=Messages.INVALID_TOKEN)