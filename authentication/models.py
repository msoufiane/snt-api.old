from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    class Meta:
        permissions = (
            ('edit_accout', 'Can edit account'),
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
