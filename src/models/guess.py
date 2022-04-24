import sqlalchemy as sa
from models.modelbase import ModelBase


class Guess(ModelBase):
    __tablename__ = "guesses"

    guess_id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    game_id = sa.Column("game_id", sa.Integer, sa.ForeignKey("active_games.id"), nullable=False)
    word = sa.Column("text", sa.String)
