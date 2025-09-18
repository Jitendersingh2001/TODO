from pydantic import BaseModel, Field

# Base schema for shared fields
class TodoBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100,
                       description="Title of the todo, between 3 and 100 characters")
    description: str = Field(..., min_length=3, max_length=100,
                             description="Description of the todo, between 10 and 100 characters")


class TodoCreate(TodoBase):
    pass


class TodoEdit(TodoBase):
    id: int


class TodoDefault(BaseModel):
    id: int
