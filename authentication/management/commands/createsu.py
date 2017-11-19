from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from authentication.models import Account


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Account.objects.filter(username="soufiaane").exists():
            user = Account.objects.create_superuser(
                username="soufiaane",
                email="soufiaane@sentad.com",
                password="soufiane0"
            )  # TODO password from env
            [user.user_permissions.add(permission) for permission in Permission.objects.all()]
