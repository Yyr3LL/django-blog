from django.db import models
from django.utils import timezone


class Post(models.Model):

    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

