from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=101)
    description = models.TextField()
    Views= models.IntegerField()
    lengthh = models.CharField(max_length=20)
    pubdate= models.DateField()
    channel_name = models.CharField(max_length=1000)
    requestdate=models.DateField()
    def __str__(self):
        return self.title