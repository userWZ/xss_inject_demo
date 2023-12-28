import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DEFAULT_DATE = datetime.datetime.now().strftime('%B %d, %Y')


class Post(models.Model):

    title = models.CharField(max_length=64)
    category = models.CharField(max_length=16)
    content = models.TextField()
    date_posted = models.DateField(default=DEFAULT_DATE)

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id)