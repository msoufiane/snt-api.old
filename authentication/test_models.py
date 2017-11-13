from django.test import TestCase
from authentication.models import Account


class AuthenticationTestCase(TestCase):
    def setUp(self):
        Account.objects.create_superuser(username="admin", email="admin@sentad.com", password="supers3cr3t")

    def test_account(self):
        admin = Account.objects.get(username="admin")
        self.assertEqual(admin.is_admin, True)
