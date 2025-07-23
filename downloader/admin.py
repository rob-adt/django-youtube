from django.contrib import admin
from .models import Video
from .models import Request

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display=('title', 'requestdate', 'channel_name','pubdate','lengthh','Views')
    search_fields=('title','description','channel_name')
    list_filter=('channel_name','pubdate','requestdate')

admin.site.register(Video, VideoAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display=('stringdate',"title","channel_name")
    search_fields=('requestdate',"title","channel_name")
    list_filter=('requestdate',"title","channel_name")

admin.site.register(Request,RequestAdmin)

