from typing import Optional

from starlette import status
from pydantic import BaseModel

from src.schemas.enums import Language, WordDifficulty


class BaseWordModel(BaseModel):
    pass


class GetWordModel(BaseModel):
    id: int
    word: str
    translation: str
    language: Language
    description: Optional[str] = None
    difficulty: WordDifficulty


class PostReqWordModel(BaseWordModel):
    word: str
    translation: str
    language: Language
    description: Optional[str] = None
    difficulty: WordDifficulty


class PostRespWordModel(BaseModel):
    status: int
    id: int


class PatchWordModel(BaseWordModel):
    word: Optional[str] = None
    translation: Optional[str] = None
    language: Language = Language.FRENCH
    description: Optional[str] = None
    difficulty: WordDifficulty = WordDifficulty.EASY
