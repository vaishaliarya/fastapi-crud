from fastapi import Request,status
from fastapi.responses import JSONResponse, Response

from app.exceptions.todonotfoundexception import TodoNotFoundException


async def to_do_not_found_handler(
        request: Request,
        excep: TodoNotFoundException) -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": {
                "type": "TodoNotFoundError",
                "message": excep.detail,
                "path": str(request.url)
            }
        }
    )
