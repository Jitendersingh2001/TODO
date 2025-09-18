from typing import Tuple
from sqlalchemy.orm import Session
from fastapi import Depends
from app.config.database import get_db
from app.utils.auth import get_authenticate

def get_user_and_db(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_authenticate)
) -> Tuple[dict, Session]:
    """
    Returns both the current user and DB session.
    """
    return current_user, db
