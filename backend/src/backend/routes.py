from fastapi import APIRouter, HTTPException
from sqlmodel import select

from backend.database import SessionDep
from backend.models import Todo, TodoCreate, TodoRead, TodoUpdate

router = APIRouter(prefix='/todos', tags=["todos"])

@router.post("", response_model=TodoRead,status_code=200)
def create_todo(todo_in:TodoCreate, session:SessionDep):
    todo=Todo.model_validate(todo_in)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.get("",response_model=list[TodoRead])
def list_todos(session:SessionDep):
    return session.exec(select(Todo)).all()

@router.get("/{todo+id}",response_model=TodoRead)
def get_todo(todo_id:int, session:SessionDep):
    todo = session.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not Found")
    return todo

@router.patch("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id:int, todo_in: TodoUpdate, session:SessionDep):
    todo = session.get(Todo,todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not Found")
    todo.sqlmodel_update(todo_in.model_dump(exclude_unset=True))
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id:int,session: SessionDep):
    todo=session.het(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not Found")
    session.delete(todo)
    session.commit()