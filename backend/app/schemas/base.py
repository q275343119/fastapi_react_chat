from typing import TypeVar, Generic, Optional

from pydantic.generics import GenericModel

T = TypeVar('T')


class ResultModel(GenericModel, Generic[T]):
    code: int = 200
    msg: str = 'success'
    data: Optional[T] = None
