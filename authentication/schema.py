import graphene

from graphene_django.types import DjangoObjectType

from authentication.models import Account


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class Query(graphene.AbstractType):
    all_accounts = graphene.List(AccountType)

    def resolve_all_accounts(self, info, **kwargs):
        return Account.objects.all()
