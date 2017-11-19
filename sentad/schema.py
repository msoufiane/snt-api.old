from authentication.schema import AccountQuery, PermissionQuery, GroupQuery, CreateGroup
import graphene


class Mutation(graphene.ObjectType):
    create_group = CreateGroup.Field()


class Query(
    PermissionQuery,
    AccountQuery,
    GroupQuery,
    # Finally import graphene ObjectType
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
