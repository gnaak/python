from django.db import models
from accounts.models import User
# Create your models here.

class Todo(models.Model):
    author = models.TextField()
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)