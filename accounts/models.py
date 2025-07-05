from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    address = models.TextField(blank=True, null=True)
    is_store_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.username

