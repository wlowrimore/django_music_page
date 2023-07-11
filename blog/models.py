from personal_portfolio import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# class Snippet(models.Model):
#     user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
#     blogname = models.CharField(max_length=100)
#     blogauth = models.CharField(max_length=100)
#     blogdes = models.TextField(max_length=400)
#     img = models.ImageField(upload_to='pics')
#
#     def __str__(self):
#         return self.blogname


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.author}, {0.body}'
        return template.format(self)
