import sqlalchemy as sa
from models.modelbase import ModelBase


class Word(ModelBase):
    __tablename__ = "words"

    word_id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    text = sa.Column("text", sa.String)
    is_simple = sa.Column("is_simple", sa.Boolean, default=False)
