from django.contrib.auth.models import Group, Permission
from graphene_django.types import DjangoObjectType
from authentication.models import Account
import graphene


class PermissionType(DjangoObjectType):
    class Meta:
        model = Permission


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        only_fields = ('username', 'first_name', 'last_name', 'email', 'groups', 'user_permissions')


class GroupType(DjangoObjectType):
    class Meta:
        model = Group

    id = graphene.ID
    name = graphene.String
    permissions = graphene.List(PermissionType)
    user_set = graphene.List(AccountType)


class AccountQuery(graphene.ObjectType):
    permissions = graphene.List(PermissionType)
    accounts = graphene.List(AccountType)
    groups = graphene.List(GroupType)

    def resolve_accounts(self, info, **kwargs):
        return Account.objects.all()

    def resolve_permissions(self, info, **kwargs):
        return Account.objects.select_related("user_permissions")

    def resolve_groups(self, info, **kwargs):
        return Account.objects.select_related("groups")


class PermissionQuery(graphene.ObjectType):
    permissions = graphene.List(PermissionType)

    def resolve_permissions(self, info, **kwargs):
        return Permission.objects.all()


class GroupQuery(graphene.ObjectType):
    groups = graphene.List(GroupType)

    @staticmethod
    def resolve_groups(info, **kwargs):
        return Group.objects.all()


class CreateGroup(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    form_errors = graphene.String
    group = graphene.Field(lambda: Group)

    def mutate(self, info, **args):
        group = Group.objects.create(name=args.get("name"))
        return CreateGroup(group=group , form_errors=None)
