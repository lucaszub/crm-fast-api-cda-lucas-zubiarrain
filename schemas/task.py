from pydantic import BaseModel
from datetime import date

class TaskBase(BaseModel):
    title: str
    description: str
    due_date: date
    id_user: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: str = None
    description: str = None
    due_date: date = None

class Task(TaskBase):
    id_task: int

    class Config:
        orm_mode = True
