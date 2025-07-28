from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(url=settings.DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine)


# Dependency
async def get_db() -> AsyncGenerator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()


from models import user


# Создание всех таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Удаление всех таблиц
async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
