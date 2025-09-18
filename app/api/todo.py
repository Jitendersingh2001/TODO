from fastapi import APIRouter, Depends
from app.services.todo_service import TodoService
from app.dependencies.user_and_db import get_user_and_db
from app.schemas.todo import TodoCreate, TodoDefault, TodoEdit

router = APIRouter(prefix="/todo", tags=["todo"])

@router.post("/")
def create_todo(todo: TodoCreate, user_db: tuple = Depends(get_user_and_db)):
    current_user, db = user_db
    service = TodoService(db)
    return service.create_todo(current_user['user_id'], todo.title, todo.description)

@router.put("/")
def complete_todo(todo: TodoDefault, user_db: tuple = Depends(get_user_and_db)):
    service = TodoService(user_db[1])
    return service.complete_todo(todo.id)

@router.delete("/")
def delete_todo(todo: TodoDefault, user_db: tuple = Depends(get_user_and_db)):
    service = TodoService(user_db[1])
    return service.delete_todo(todo.id)

@router.put("/editTask")
def edit_todo(todo: TodoEdit, user_db: tuple = Depends(get_user_and_db)):
    service = TodoService(user_db[1])
    return service.edit_todo(todo.id, todo.title, todo.description)

@router.get("/getTodos")
def get_todos(user_db: tuple = Depends(get_user_and_db)):
    current_user, db = user_db
    service = TodoService(db)
    return service.get_todos(current_user['user_id'])