from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User


async def create_user(
        session: AsyncSession,
        username: str,
) -> int:
    obj = User(
        username=username,
    )

    session.add(obj)
    await session.flush()
    await session.commit()

    return obj.id


async def get_user_by_id(
        session: AsyncSession,
        user_id: int,
):

    obj = await session.get(User, user_id)

    return obj


async def get_user_by_username(
        session: AsyncSession,
        username: str,
) -> Optional[User]:

    stmt = (
        select(User)
        .where(User.username == username)
    )
    result = await session.execute(stmt)
    result = result.scalar_one_or_none()

    return result


async def get_user_by_username_or_create(
        session: AsyncSession,
        username: str,
) -> User:

    result = await get_user_by_username(
        session=session,
        username=username,
    )

    if result is None:
        result_id = await create_user(
            session=session,
            username=username,
        )
        result = await get_user_by_id(
            session=session,
            user_id=result_id,
        )

    return result
