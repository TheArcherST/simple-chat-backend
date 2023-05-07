import asyncio
from datetime import datetime
from typing import Optional
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

from .database import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(default=None)


class Message(Base):
    __tablename__ = 'message'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    from_user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    chat_id: Mapped[int] = mapped_column(ForeignKey(User.id))  # only p2p dialogs are supports
    text: Mapped[str] = mapped_column()
    received_at: Mapped[Optional[datetime]] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(default=None)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
