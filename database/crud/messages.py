import datetime
from typing import Optional, Iterable

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession


from ..models import Message


async def send_message(
        session: AsyncSession,
        from_user_id: int,
        chat_id: int,
        text: str,
) -> int:

    obj = Message(
        from_user_id=from_user_id,
        chat_id=chat_id,
        text=text,
    )

    session.add(obj)
    await session.flush()
    await session.commit()

    return obj.id


async def mark_message_as_received(
        session: AsyncSession,
        message_id: int,
) -> None:

    message = await session.get(Message, message_id)

    message.received_at = datetime.datetime.utcnow()

    await session.flush()
    await session.commit()

    return None


async def get_unreceived_messages(
        session: AsyncSession,
        for_user_id: int,
) -> Iterable[Message]:

    stmt = (select(Message)
            .where(Message.chat_id == for_user_id)
            .where(Message.from_user_id != for_user_id)
            .where(Message.received_at.is_(None)))

    result = await session.execute(stmt)
    result = result.scalars()

    return result


async def mark_messages_as_received(
        session: AsyncSession,
        message_ids: list[int],
) -> None:

    stmt = (update(Message)
            .where(Message.id.in_(message_ids))
            .values(received_at=datetime.datetime.utcnow()))

    await session.execute(stmt)
    await session.commit()

    return None
