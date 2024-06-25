from typing import List, Annotated
from starlette import status
from fastapi import APIRouter, Depends, Response

from src.schemas.words import GetWordModel, PostReqWordModel, PostRespWordModel, PatchWordModel
from src.repositories.word_repository import WordRepository

router = APIRouter(prefix="/words", tags=["words"])


@router.get("/", response_model=List[GetWordModel])
async def get_words() -> List[GetWordModel]:
    words = await WordRepository.get_words()
    return words


@router.post("/")
async def add_word(word: Annotated[PostReqWordModel, Depends()]) -> PostRespWordModel:
    word_id = await WordRepository.add_word(word)
    return {"status": status.HTTP_200_OK, "id": word_id}


@router.patch("/{word_id}")
async def change_word(word_id: int, data: Annotated[PatchWordModel, Depends()]) -> PostRespWordModel:
    word_id = await WordRepository.patch_word(word_id, data)
    return {"status": status.HTTP_200_OK, "id": word_id}
