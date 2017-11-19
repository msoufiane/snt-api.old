from authentication.schemaTypes import AccountType, GroupType, PermissionType
from django.contrib.auth.models import Group, Permission
from authentication.models import Account
import graphene


# region Queries
class MeQuery(graphene.ObjectType):
    me = graphene.Field(AccountType)

    def resolve_me(self, info):
        if info.context.user.is_anonymous():
            return Account.objects.get(username="soufiaane")  # TODO return None
        return Account.objects.get(username=info.context.user.username)


class GroupsQuery(graphene.ObjectType):
    groups = graphene.List(GroupType)

    def resolve_groups(self, info):
        return Group.objects.all()


class PermissionQuery(graphene.ObjectType):
    permissions = graphene.List(PermissionType)

    def resolve_permissions(self, info):
        return Permission.objects.all()
# endregion


# region Mutations
class CreateGroup(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    form_errors = graphene.String()
    group = graphene.Field(lambda: GroupType)

    def mutate(self, info, name=None):
        group = Group.objects.create(name=name)
        return CreateGroup(group=group)
# endregion
