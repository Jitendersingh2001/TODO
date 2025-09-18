from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.todo_service import TodoService

router = APIRouter(prefix="/todo", tags=["todo"])