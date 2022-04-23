import graphene
from graphene import relay, ResolveInfo
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from logic.make_guess import make_guess
from logic.random_word import get_random_word
from models.word import Word as WordModel
from logic.start_game import start_game
from schema.types import Hint


class Word(SQLAlchemyObjectType):
    class Meta:
        model = WordModel
        interfaces = (relay.Node,)


class Guess(graphene.Mutation):
    class Arguments:
        guess = graphene.String(required=True)
        session_id = graphene.Int(required=True)

    has_won = graphene.Boolean()
    hints = graphene.List(graphene.NonNull(Hint), required=True)

    def mutate(self: graphene.Mutation, info: ResolveInfo, guess: str, session_id: int) -> graphene.Mutation:
        hints = make_guess(guess, session_id)
        return Guess(has_won=False, hints=hints)


class StartGame(graphene.Mutation):
    class Arguments:
        pass

    game_id = graphene.Int()

    def mutate(self: graphene.Mutation, info: ResolveInfo) -> graphene.Mutation:
        game_id = start_game()
        return StartGame(game_id=game_id)


class Mutations(graphene.ObjectType):
    make_guess = Guess.Field()
    start_game = StartGame.Field()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_words = SQLAlchemyConnectionField(Word.connection)

    random_word = graphene.Field(Word)

    def resolve_random_word(self: graphene.ObjectType, info: ResolveInfo) -> WordModel:
        return get_random_word(True)


schema = graphene.Schema(query=Query, mutation=Mutations)
