from fastapi import APIRouter, Depends
from app.services.todo_service import TodoService
from app.dependencies.user_and_db import get_user_and_db
from app.schemas.todo import TodoCreate

router = APIRouter(prefix="/todo", tags=["todo"])

@router.post("/")
def create_todo(todo: TodoCreate, user_db: tuple = Depends(get_user_and_db)):
    current_user, db = user_db
    service = TodoService(db)
    return service.create_todo(current_user['user_id'], todo.title, todo.description)