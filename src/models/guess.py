from enum import Enum
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from models.modelbase import ModelBase


class Color(Enum):
    GREY = 'GREY'
    YELLOW = 'YELLOW'
    GREEN = 'GREEN'


class Guess(ModelBase):
    __tablename__ = "guesses"

    guess_id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    game_id = sa.Column("game_id", sa.Integer, sa.ForeignKey("active_games.id"), nullable=False)
    word = sa.Column("text", sa.String)
    hints = relationship("Hint", back_populates="guess")
