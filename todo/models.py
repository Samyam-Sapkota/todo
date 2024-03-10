from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    mission =models.CharField(max_length=200)

    status=models.BooleanField(default=False)

    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.mission