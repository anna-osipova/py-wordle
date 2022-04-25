from typing import List

from flask import g

from models.active_game import ActiveGame
from models.guess import Guess, Color
from models.hint import Hint


def make_guess(guess_word: str, session_id: int) -> List[Hint]:
    game = g.session.query(ActiveGame).filter(ActiveGame.game_id == session_id).one()

    # TODO: check if game is over
    # TODO: check if guess word is a real word
    assert len(guess_word) == 5
    hints = []

    guess = Guess(word=guess_word, game_id=session_id)
    
    for index in range(5):
        color = get_letter_color(game.word, guess_word, index)
        hint = Hint(letter=guess_word[index], color=color, guess_id=guess.guess_id)
        hints.append(hint)

    guess.hints = hints
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
