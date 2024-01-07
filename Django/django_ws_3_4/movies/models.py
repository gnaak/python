from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.TextField()
    genre = models.TextField()
    director = models.CharField(max_length=20, default='UnKnown')