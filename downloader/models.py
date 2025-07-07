from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.CharField(max_length=500)
    dsc = models.TextField()
    title = models.CharField(max_length=101)
    views= models.IntegerField()
    vid_length = models.CharField(max_length=20)
    pubdate= models.DateField()
    channel_name = models.CharField(max_length=1000)