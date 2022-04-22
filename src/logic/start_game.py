from flask import g

from logic.random_word import get_random_word
from models.active_game import ActiveGame


def start_game() -> int:
    word = get_random_word(is_simple=True)
    game = ActiveGame(word=word.text)
    g.session.add(game)
    g.session.commit()
    return game.game_id
