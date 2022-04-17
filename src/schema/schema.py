import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.word import Word as WordModel


class Word(SQLAlchemyObjectType):
    class Meta:
        model = WordModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_words = SQLAlchemyConnectionField(Word.connection)


schema = graphene.Schema(query=Query)
