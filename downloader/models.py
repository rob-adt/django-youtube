from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.CharField(max_length=500)
    