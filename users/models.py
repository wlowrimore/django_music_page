from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import path

from personal_portfolio import settings


class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return path.join('Users', self.username, instance)
        return None

    class Meta:
        db_table = "auth_user"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='profile',  on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(max_length=254, default='')
    location = models.CharField(max_length=101, default='')
    bio = models.TextField(max_length=254, default='')
    profile_img = models.ImageField(default='no_image.png', upload_to='profile_images')

    def __str__(self):
        return self.user.username
