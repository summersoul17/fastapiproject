from enum import Enum


class WordDifficulty(Enum):
    EASY = "Легко"
    MEDIUM = "Средне"
    HARD = "Сложно"


class Language(Enum):
    ENGLISH = "Английский"
    FRENCH = "Французский"


class PartOfSpeech(Enum):
    NOUN = "Существительное"
    ADJECTIVE = "Прилагательное"
    VERB = "Глагол"
    ADVERB = "Наречие"
    NUMERAL = "Числительное"
    PRONOUN = "Местоимение"
    PREPOSITION = "Предлог"
    CONJUNCTION = "Союз"
    ARTICLE = "Артикль"


class WordGender(Enum):
    FEMININE = "Ж"
    MASCULINE = "М"


class OrderBy(str, Enum):
    WordDifficulty = "word_difficulty"
    Language = "language"
    PartOfSpeech = "part_of_speech"
    WordGender = "word_gender"
    Word = "word"
