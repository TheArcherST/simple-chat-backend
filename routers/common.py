from typing_extensions import TypeAlias
from typing import AsyncGenerator

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database import crud
from database.models import User
from database.database import engine


SessionType: TypeAlias = AsyncSession


async def database_session() -> AsyncGenerator[SessionType, None]:
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session


async def authenticated_user(
        session: SessionType = Depends(database_session),
        my_username: str = ...,
) -> User:

    user = await crud.user.get_user_by_username_or_create(
        session=session,
        username=my_username,
    )

    yield user
