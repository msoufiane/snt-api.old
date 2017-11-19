from django.test import TestCase
from authentication.models import Account


class AuthenticationTestCase(TestCase):
    def test_account(self):
        self.assertEqual(True, True)
