from typing import Literal

from fastapi import status
from pydantic import BaseModel

from utils.schema_errors import HTTPExceptionWrapper


class Exceptions:
    class PermissionDenied(HTTPExceptionWrapper):
        __status_code__ = status.HTTP_403_FORBIDDEN
        __detail__ = 'permission denied'

    class UserNotFound(HTTPExceptionWrapper):
        __status_code__ = status.HTTP_404_NOT_FOUND
        __detail__ = 'user not found'

    class ChatNotFound(HTTPExceptionWrapper):
        __status_code__ = status.HTTP_404_NOT_FOUND
        __detail__ = 'chat not found'


class Schemas:
    class PermissionDenied(BaseModel):
        detail: Literal['permission denied']

    class UserNotFound(BaseModel):
        detail: Literal['user not found']

    class ChatNotFound(BaseModel):
        detail: Literal['chat not found']
