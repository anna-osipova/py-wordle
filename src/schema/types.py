import graphene


class Hint(graphene.ObjectType):
    letter = graphene.String()
    color = graphene.String()
