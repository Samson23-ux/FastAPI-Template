from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class SuccessResponse(BaseModel, Generic[T]):
    status: str = "success"
    message: str | None = None
    data: T | list[T] | None = None


class AllSuccessResponse(SuccessResponse):
    cursor: str | None = None


class Error(BaseModel):
    code: str
    message: str
    request_id: UUID
    details: dict[str, str] | None = None


class ErrorResponse(BaseModel):
    error: Error
