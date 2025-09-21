from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.connection import get_db
from app.exceptions.todonotfoundexception import TodoNotFoundException
from app.model.todomodel import Todo
from app.schema.todoResponse import TodoResponse
from app.schema.todocreate import TodoCreate

router=APIRouter()

@router.post(path="/add-todo",response_model=TodoResponse)
def create_todo(todo:TodoCreate,db:Session=Depends(get_db)):
    db_todo=Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return TodoResponse(description=f"Description: {db_todo.description}, Todo_Status: {db_todo.status}", status="Created")

@router.get(path="/get-todo/{tid}",response_model=TodoResponse)
def get_todo_byid(tid:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==tid).first()
    if not todo:
        raise HTTPException(status_code=404,detail="record does not exist")
    return todo

@router.delete(path="/del-todo/{tid}",response_model=TodoResponse)
def del_todo_byid(tid:int,db:Session=Depends(get_db)):
   db_todo=db.query(Todo).filter(Todo.id==tid).first()
   if not db_todo:
       raise HTTPException(status_code=404,detail="Record does not exist")
   db.delete(db_todo)
   db.commit()
   return db_todo

@router.put(path="/update-todo/{tid}", response_model=TodoResponse,
            responses={404: {"description": "Employee not found"}},)
def update_todo(tid:int,todo:TodoCreate,db:Session=Depends(get_db)):
    db_todo=db.query(Todo).filter(Todo.id==tid).first()
    if not db_todo:
       raise TodoNotFoundException(f"The Todo of id {tid} does not exist")
    db_todo.description=todo.description
    db.commit()
    db.refresh(db_todo)

    return db_todo