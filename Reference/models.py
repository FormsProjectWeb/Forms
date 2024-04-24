from django.db import models
from django.urls import reverse

class Reference(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Subject')
    topics = models.TextField(verbose_name='Topics')

class Response(models.Model):
    subject = models.TextField()
    topics = models.TextField()