from django.db import models

# Create your models here.
class Garages(models.Model):
    location = models.TextField()
    capacity = models.IntegerField()
    is_parking_available = models.BooleanField()
    opening_time = models.TimeField("", auto_now=False, auto_now_add=False)
    closing_time = models.TimeField("", auto_now=False, auto_now_add=False)