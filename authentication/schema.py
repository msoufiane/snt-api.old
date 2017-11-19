from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import Group, Permission
from authentication.models import Account
import graphene


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        only_fields = ('username', 'first_name', 'last_name', 'email', 'groups', 'user_permissions')


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class PermissionType(DjangoObjectType):
    class Meta:
        model = Permission


class accountQuery(graphene.ObjectType):
    permissions = graphene.List(PermissionType)
    accounts = graphene.List(AccountType)
    groups = graphene.List(GroupType)

    def resolve_accounts(self, info, **kwargs):
        return Account.objects.all()

    def resolve_permissions(self, info, **kwargs):
        return Permission.objects.all()

    def resolve_groups(self, info, **kwargs):
        return Group.objects.all()
