from typing_extensions import Self
from typing import Optional

from dataclasses import dataclass
from datetime import datetime

from database import models
from schemas.v1 import message as schemas

from .base import BaseDataIntermediary


@dataclass
class MessageDataIntermediary(BaseDataIntermediary):
    id: int
    from_user_id: int
    chat_id: int
    text: str
    received_at: Optional[datetime]
    created_at: Optional[datetime]
    deleted_at: Optional[datetime]

    @classmethod
    def from_model(cls, obj: models.Message) -> Self:
        return cls(
            id=obj.id,
            from_user_id=obj.from_user_id,
            chat_id=obj.chat_id,
            text=obj.text,
            received_at=obj.received_at,
            created_at=obj.created_at,
            deleted_at=obj.deleted_at,
        )

    def to_schema(self) -> schemas.Message:
        return schemas.Message(
            id=self.id,
            from_user_id=self.from_user_id,
            chat_id=self.chat_id,
            text=self.text,
        )
