import graphene
from authentication.schema import Query as authenticationQuery


class Query(
    authenticationQuery,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
