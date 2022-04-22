import sqlalchemy as sa
from models.modelbase import ModelBase


class ActiveGame(ModelBase):
    __tablename__ = "active_games"

    game_id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    word = sa.Column("text", sa.String)
