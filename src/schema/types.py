import graphene

from models.guess import Color


class Hint(graphene.ObjectType):
    letter = graphene.String()
    color = graphene.Field(graphene.Enum.from_enum(Color))
