from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
