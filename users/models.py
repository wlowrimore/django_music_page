from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import path


class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return path.join('Users', self.username, instance)
        return None

    description = models.TextField(default='')
    profile_img = models.ImageField(default='img/no_image.png', upload_to='img/')

    class Meta:
        db_table = "auth_user"
