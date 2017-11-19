from authentication.schema import MeQuery, PermissionQuery, GroupsQuery, CreateGroup
import graphene


class Query(MeQuery, GroupsQuery, PermissionQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_group = CreateGroup.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
