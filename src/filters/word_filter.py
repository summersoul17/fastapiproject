from typing import Optional

from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from src.schemas.enums import Language, WordDifficulty, PartOfSpeech
from src.database.models import WordORM


class WordFilter(Filter):
    language: Optional[Language] = None
    difficulty: Optional[WordDifficulty] = None
    part_of_speech: Optional[PartOfSpeech] = None

    class Constants(Filter.Constants):
        model = WordORM
        search_model_fields = ["language", "difficulty", "part_of_speech"]

