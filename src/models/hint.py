import sqlalchemy as sa
from sqlalchemy.orm import relationship
from models.guess import Color
from models.modelbase import ModelBase


class Hint(ModelBase):
    __tablename__ = "hints"

    hint_id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    guess_id = sa.Column("guess_id", sa.Integer, sa.ForeignKey("guesses.id"), nullable=False)
    letter = sa.Column("letter", sa.String(1), nullable=False)
    color = sa.Column("color", sa.Enum(Color), nullable=False)
    guess = relationship("Guess", back_populates="hints")
