from typing import List

from fastapi import Depends
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import async_session
from src.database.models import WordORM
from src.schemas.words import GetWordModel, PostRespWordModel, PostReqWordModel, PatchWordModel


class WordRepository:
    @classmethod
    async def add_word(
            cls,
            word: PostReqWordModel):
        async with async_session() as session:
            word_dict = word.model_dump()
            word_orm = WordORM(**word_dict)
            session.add(word_orm)
            await session.flush()
            await session.commit()
            return word_orm.id

    @classmethod
    async def get_words(cls) -> List[GetWordModel]:
        async with async_session() as session:
            query = select(WordORM).order_by(WordORM.word.asc())
            result = await session.execute(query)
            word_models = result.scalars().all()
            validated_data = [GetWordModel.model_validate(word_model.__dict__) for word_model in word_models]
            return validated_data
    @classmethod
    async def patch_word(cls, word_id: int, word: PatchWordModel):
        async with async_session() as session:
            word_dict = word.model_dump()
            instance = await session.get(WordORM, word_id)
            for key, value in word_dict.items():
                if value:
                    setattr(instance, key, value)
            await session.flush()
            await session.commit()
            return word_id
