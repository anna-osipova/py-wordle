from typing import List

from flask import g

from models.active_game import ActiveGame
from models.guess import Guess, Color
from schema.types import Hint


def make_guess(guess: str, session_id: int) -> List[Hint]:
    game = g.session.query(ActiveGame).filter(ActiveGame.game_id == session_id).one()

    # TODO: check if game is over
    # TODO: check if guess word is a real word
    assert len(guess) == 5
    hints = []

    for index in range(5):
        color = get_letter_color(game.word, guess, index)
        hints.append(Hint(letter=guess[index], color=color))

    guess = Guess(word=guess, game_id=session_id)
    g.session.add(guess)
    g.session.commit()

    return hints


def get_letter_color(word: str, guess: str, index: int) -> Color:
    if word[index] == guess[index]:
        return Color.GREEN

    letter = guess[index]
    if letter not in word:
        return Color.GREY

    # TODO: improve yellow logic
    return Color.YELLOW
