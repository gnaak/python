from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=200)
    issue_b = models.CharField(max_length=200)

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField(default=False)
    content = models.CharField(max_length=100)
