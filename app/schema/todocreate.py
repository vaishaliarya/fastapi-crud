from fastapi import HTTPException


from fastapi.datastructures import Default
from pydantic import BaseModel, Field, field_validator
from pydantic.v1 import validator

from app.util.todo_status import TodoStatus
from datetime import date

class TodoCreate(BaseModel):
    description : str =Field(max_length=50,min_length=5,description="Todo Description")
    status:TodoStatus
    due_date:date

    @field_validator("due_date")
    def not_due_date(cls,d):
        if d<date.today():
            raise HTTPException(status_code=400,detail="Due date can not be a past date")