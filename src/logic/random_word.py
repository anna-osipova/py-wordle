from random import randint
from typing import Optional

from flask import g

from models.word import Word


def get_random_word(is_simple: Optional[bool] = False) -> Word:
    queries = [Word.is_simple == is_simple] if is_simple else []
    words = g.session.query(Word).filter(*queries).all()
    return words[randint(0, len(words) - 1)]
