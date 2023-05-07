import asyncio

from typing_extensions import Self

from typing import Generic, TypeVar, Iterable

from sqlalchemy.ext.asyncio import AsyncSession


_MT = TypeVar("_MT")
_ST = TypeVar("_ST")


class BaseDataIntermediary(Generic[_MT, _ST]):
    @classmethod
    async def from_model(cls, obj: _MT) -> Self:
        raise NotImplementedError

    async def to_schema(self, session: AsyncSession) -> _ST:
        raise NotImplementedError

    @classmethod
    async def model_to_schema(cls, session: AsyncSession, obj: _MT) -> _ST:
        return await (await cls.from_model(obj)).to_schema(session)

    @classmethod
    async def models_to_schemas(cls, session: AsyncSession, objs: Iterable[_MT]) -> Iterable[_ST]:
        return await asyncio.gather(*(cls.model_to_schema(session, i) for i in objs))
