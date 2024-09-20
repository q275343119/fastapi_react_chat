from functools import wraps

from app.schemas.base import ResultModel


def response_wrapper(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        res = ResultModel()
        data = await func(*args, **kwargs)
        res.data = data
        return res

    return wrapper
