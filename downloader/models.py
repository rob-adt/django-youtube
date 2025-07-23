from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.CharField(max_length=500,null=True, blank=True)
    title = models.CharField(max_length=101,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    Views= models.IntegerField(null=True, blank=True)
    lengthh = models.CharField(max_length=20,null=True, blank=True)
    pubdate= models.DateField(null=True, blank=True)
    channel_name = models.CharField(max_length=1000,null=True, blank=True)
    requestdate=models.DateField(null=True, blank=True)
    timereq=models.CharField(max_length=20,null=True, blank=True)
    requests=models.IntegerField(default=0,null=True, blank=True)
    def __str__(self):
        return self.title
    
class Request(models.Model):
    url = models.CharField(max_length=500, null=True, blank=True)
    keys=models.ForeignKey(Video,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=101,null=True, blank=True)
    requestdate=models.DateField(null=True, blank=True)
    channel_name = models.CharField(max_length=1000,null=True, blank=True)
    timereq=models.CharField(max_length=20,null=True, blank=True)
    stringdate= models.CharField(max_length=1000,null=True, blank=True)
    def __str__(self):
        return self.stringdate