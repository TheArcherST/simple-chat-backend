from typing_extensions import Self

from typing import Generic, TypeVar, Iterable


_MT = TypeVar("_MT")
_ST = TypeVar("_ST")


class BaseDataIntermediary(Generic[_MT, _ST]):
    @classmethod
    def from_model(cls, obj: _MT) -> Self:
        raise NotImplementedError

    def to_schema(self) -> _ST:
        raise NotImplementedError

    @classmethod
    def model_to_schema(cls, obj: _MT) -> _ST:
        return cls.from_model(obj).to_schema()

    @classmethod
    def models_to_schemas(cls, objs: Iterable[_MT]) -> Iterable[_ST]:
        return (cls.from_model(i).to_schema() for i in objs)
