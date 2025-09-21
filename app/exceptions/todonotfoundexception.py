from fastapi import HTTPException
from starlette import status


class TodoNotFoundException(Exception):
    def __init__(self,detail:str):
        self.detail=detail
        super().__init__( self.detail)
