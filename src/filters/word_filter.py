from typing import Optional

from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from src.schemas.enums import Language, WordDifficulty, PartOfSpeech, WordGender
from src.database.models import WordORM


class WordFilter(Filter):
    language: Optional[Language] = None
    difficulty: Optional[WordDifficulty] = None
    part_of_speech: Optional[PartOfSpeech] = None
    word_gender: Optional[WordGender] = None

    class Constants(Filter.Constants):
        model = WordORM
        search_model_fields = ["language", "difficulty", "part_of_speech", "word_gender"]

