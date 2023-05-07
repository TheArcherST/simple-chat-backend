from typing_extensions import Self
from typing import Optional

from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from database import models, crud
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
    async def from_model(cls, obj: models.Message) -> Self:
        return cls(
            id=obj.id,
            from_user_id=obj.from_user_id,
            chat_id=obj.chat_id,
            text=obj.text,
            received_at=obj.received_at,
            created_at=obj.created_at,
            deleted_at=obj.deleted_at,
        )

    async def to_schema(self, session: AsyncSession) -> schemas.Message:
        user = await crud.user.get_user_by_id(
            session=session,
            user_id=self.from_user_id
        )

        return schemas.Message(
            id=self.id,
            from_user=user.username,
            chat=user.username,
            text=self.text,
        )
