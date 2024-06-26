from typing import List, Annotated, Optional

from fastapi_filter import FilterDepends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from fastapi import APIRouter, Depends, Response, Query

from src.database.database import get_async_session
from src.database.models import WordORM
from src.filters.word_filter import WordFilter
from src.schemas.enums import OrderBy
from src.schemas.words import GetWordModel, PostReqWordModel, PostRespWordModel, PatchWordModel

router = APIRouter(prefix="/words", tags=["words"])


@router.get("/", response_model=List[GetWordModel], status_code=status.HTTP_200_OK)
async def get_words(
        order_by: Optional[OrderBy] = Annotated[OrderBy, Depends()],
        word_filter: WordFilter = FilterDepends(WordFilter),
        limit: Optional[int] = Query(10),
        offset: Optional[int] = Query(0),
        session: AsyncSession = Depends(get_async_session)
) -> List[GetWordModel]:
    try:
        query = select(WordORM).order_by(getattr(WordORM, order_by))
    except TypeError:
        query = select(WordORM).order_by(WordORM.word)
    query = word_filter.filter(query)
    result = await session.execute(query)
    words = [GetWordModel.model_validate(word) for word in result.scalars().all()[offset:offset + limit]]
    return words


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_word(
        word_data: Annotated[PostReqWordModel, Depends()],
        session: AsyncSession = Depends(get_async_session)) -> PostRespWordModel:
    word = WordORM(**word_data.model_dump())
    session.add(word)
    await session.flush()
    await session.commit()
    return PostRespWordModel(status=status.HTTP_201_CREATED, id=word.id)


@router.patch("/{word_id}", status_code=status.HTTP_200_OK)
async def change_word(
        word_id: int,
        fields: Annotated[PatchWordModel, Depends()],
        session: AsyncSession = Depends(get_async_session)) -> PostRespWordModel:
    word = await session.get(WordORM, word_id)
    for key, value in fields:
        if value:
            setattr(word, key, value)
    await session.commit()
    return PostRespWordModel(status=status.HTTP_200_OK, id=word_id)


@router.delete("/{word_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_word(word_id: int, session: AsyncSession = Depends(get_async_session)):
    word = await session.get(WordORM, word_id)
    await session.delete(word)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
