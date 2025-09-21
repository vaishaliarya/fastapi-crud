from pydantic import BaseModel
from fastapi import status

class TodoResponse(BaseModel):
    description:str
    status : str


    class Config:
        orm_mode=True