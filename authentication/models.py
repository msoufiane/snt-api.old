from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')
        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
        )
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_superuser = True
        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    tagline = models.CharField(max_length=140, blank=True, null=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountManager()

    def __str__(self):
        """
        function that runs when applying str() fuction to the Account model
        :return: Account first name, last name, username & email address
        :rtype: str
        """
        return ' '.join([self.username, '/', self.email])

    def get_full_name(self):
        """
        overrides the AbstractBaseUser get_full_name function
        :return: Account first name + last name
        :rtype: str
        """
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        """
        overrides the AbstractBaseUser get_short_name function
        :return: Account username
        :rtype: str
        """
        return self.username
