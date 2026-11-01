from enum import StrEnum
from sqlmodel import SQLModel, Field

class Status(StrEnum):
    todo= "todo"
    finished= "finished"
    in_progress="in_progress"

class Priority(StrEnum):
    low="low"
    medium="medium"
    high="high"


class TodoBase(SQLModel):
    title: str
    description: str| None=None
    status:Status=Status.todo
    priority: Priority=Priority.medium


class Todo(TodoBase, table=True):
    id: int | None= Field(default= None, primary_key=True)
    

class TodoCreate(TodoBase): pass

class TodoUpdate(SQLModel):
    title: str | None=None
    description: str| None=None
    status: Status | None=None
    priority: Priority| None=None


class TodoRead(TodoBase):
    id:int    
