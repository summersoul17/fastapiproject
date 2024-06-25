from typing import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.database.models import Model
from src.settings import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST

engine = create_async_engine(
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}",
)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Model.metadata.create_all)


async def drop_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Model.metadata.drop_all)
