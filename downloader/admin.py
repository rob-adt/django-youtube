from django.contrib import admin
from .models import Video
from .models import Request

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display=('title', 'requestdate', 'channel_name','pubdate','lengthh','Views')
    search_fields=('title','description','channel_name')
    list_filter=('channel_name','pubdate','requestdate')

admin.site.register(Video, VideoAdmin)

admin.site.register(Request)