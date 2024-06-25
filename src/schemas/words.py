from typing import Optional
from pydantic import BaseModel

from src.schemas.enums import Language, WordDifficulty, PartOfSpeech


class BaseWordModel(BaseModel):
    pass


class GetWordModel(BaseModel):
    id: int
    word: str
    translation: str
    language: Language
    description: Optional[str] = None
    difficulty: WordDifficulty
    part_of_speech: PartOfSpeech

    class Config:
        from_attributes = True


class PostReqWordModel(BaseWordModel):
    word: str
    translation: str
    language: Language
    description: Optional[str] = None
    difficulty: WordDifficulty
    part_of_speech: PartOfSpeech

    class Config:
        from_attributes = True


class PostRespWordModel(BaseModel):
    status: int
    id: int

    class Config:
        from_attributes = True


class PatchWordModel(BaseWordModel):
    word: Optional[str] = None
    translation: Optional[str] = None
    language: Optional[Language] = None
    description: Optional[str] = None
    difficulty: Optional[WordDifficulty] = None
    part_of_speech: Optional[PartOfSpeech] = None

    class Config:
        from_attributes = True
