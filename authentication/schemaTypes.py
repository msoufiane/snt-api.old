from django.contrib.auth.models import Group, Permission
from graphene_django.types import DjangoObjectType
from authentication.models import Account


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class PermissionType(DjangoObjectType):
    class Meta:
        model = Permission


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        only_fields = ('id', 'username', 'first_name', 'last_name', 'email', 'groups', 'user_permissions')
