from django.db import models
from django.urls import reverse

class Question(models.Model):
    question = models.CharField(max_length=200, verbose_name='', blank=True)

class Response(models.Model):
    content = models.TextField()