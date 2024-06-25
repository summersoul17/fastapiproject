from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.schemas.enums import Language, WordDifficulty


class Model(DeclarativeBase):
    pass


class WordORM(Model):
    __tablename__ = 'words'

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(unique=True)
    translation: Mapped[str]
    language: Mapped[Language]
    description: Mapped[Optional[str]]
    difficulty: Mapped[WordDifficulty]
