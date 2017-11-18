from django.core.management.base import BaseCommand
from authentication.models import Account


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Account.objects.filter(username="soufiaane").exists():
            Account.objects.create_superuser("soufiaane", "soufiaane@sentad.com", "soufiane0")  # TODO password from env
