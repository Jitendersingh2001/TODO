from pydantic import BaseModel, Field

# Request schema (for creating a todo)
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100,
                       description="Title of the todo, between 3 and 100 characters")
    description: str = Field(..., min_length=3, max_length=100,
                             description="Description of the todo, between 10 and 100 characters")
