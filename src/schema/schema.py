import graphene
from graphene import relay, ResolveInfo
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.word import Word as WordModel
from random import randint


class Word(SQLAlchemyObjectType):
    class Meta:
        model = WordModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_words = SQLAlchemyConnectionField(Word.connection)

    random_word = graphene.String()

    def resolve_random_word(self: graphene.ObjectType, info: ResolveInfo) -> str:
        words = info.context['session'].query(WordModel).all()
        return words[randint(0, len(words) - 1)].text


schema = graphene.Schema(query=Query)
