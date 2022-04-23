from enum import Enum
from typing import List

from flask import g

from models.active_game import ActiveGame
from schema.types import Hint


class Color(Enum):
    GREY = 'GREY'
    YELLOW = 'YELLOW'
    GREEN = 'GREEN'


def make_guess(guess: str, session_id: int) -> List[Hint]:
    game = g.session.query(ActiveGame).filter(ActiveGame.game_id == session_id).one()

    assert len(guess) == 5
    hints = []

    for index in range(5):
        color = get_letter_color(game.word, guess, index)
        hints.append(Hint(color, guess[index]))
    return hints


def get_letter_color(word: str, guess: str, index: int) -> Color:
    if word[index] == guess[index]:
        return Color.GREEN

    letter = guess[index]
    if letter not in word:
        return Color.GREY

    return Color.YELLOW
