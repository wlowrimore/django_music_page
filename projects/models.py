from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    img = models.ImageField(upload_to='img/')
    website = models.URLField(max_length=250, default='')

    def __str__(self):
        return self.title
