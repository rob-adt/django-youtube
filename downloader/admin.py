from django.contrib import admin
from .models import Video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display=('title','channel_name','pubdate','lengthh','Views')
    search_fields=('title','description','channel_name')
    list_filter=('channel_name','pubdate','requestdate')

admin.site.register(Video)