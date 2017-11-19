from authentication.schema import accountQuery
import graphene


class Query(
    accountQuery,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
