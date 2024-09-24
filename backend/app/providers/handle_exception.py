from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import request_validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse

from app.exceptions.exception import AuthenticationError, AuthorizationError
from app.schemas.base import ResultModel


def register(app):
    @app.exception_handler(AuthenticationError)
    async def authentication_exception_handler(request: Request, e: AuthenticationError):
        """
        认证异常处理
        """
        return JSONResponse(status_code=401, content=jsonable_encoder(ResultModel(code=401, msg=e.message)))

    @app.exception_handler(AuthorizationError)
    async def authorization_exception_handler(request: Request, e: AuthorizationError):
        """
        权限异常处理
        """
        return JSONResponse(status_code=403, content=jsonable_encoder(ResultModel(code=403, msg=e.message)))

    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request: Request, exc):
        return await http_exception_handler(request, exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc):
        return await request_validation_exception_handler(request, exc)

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc):
        """
        通用异常处理
        """
        # FastApi中debug为True的时候 全局异常会失效
        return JSONResponse(status_code=500, content=jsonable_encoder(ResultModel(code=500, msg=str(exc))))
