from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"
    due_date: datetime | None = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    tasks: list[Task] = []

    class Config:
        orm_mode = True