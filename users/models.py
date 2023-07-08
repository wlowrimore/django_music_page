from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    description = models.TextField(default='')

    class Meta:
        db_table = "auth_user"
