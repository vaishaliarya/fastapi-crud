from sqlalchemy import Column, Integer, String, Date

from app.db.connection import Base
from app.util.todo_status import TodoStatus


class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    description=Column(String(45),name="desc")
    status=Column(String(45))
    due_date =Column(Date)

   