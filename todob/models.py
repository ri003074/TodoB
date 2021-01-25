from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=30)
