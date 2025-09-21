from fastapi import  FastAPI

from app.db.connection import Base, engine
from app.exceptions.todonotfoundexception import TodoNotFoundException
from app.globalhandler.custom_handler import to_do_not_found_handler
from app.router.todo_router import router as todo_router
app=FastAPI()
# Create all tables
Base.metadata.create_all(bind=engine)
app.add_exception_handler(TodoNotFoundException,to_do_not_found_handler)
app.include_router(todo_router)