from django.shortcuts import render
import datetime #imports datetime for getting the video length 
from pytubefix import YouTube #imports pytube
from pytubefix.cli import on_progress #grabs on_progress
from django.http import HttpResponse
from .models import Video
from django import forms
from django.http import FileResponse
import os
from datetime import date
# Create your views here.

def index(request):
    # return HttpResponse("Welcome to this youtube downloader website.")
    # is it a GET or a POST?
    # If POST, download video / make Video object (your choice)
    if request.method == 'GET':
        # User loads page for first time, given page with text box to put URL in
        return render(request, "downloader/index.html")
    elif request.method == 'POST':
        # We want to find the URL withon request.POST['url'] and download that video
        
        url=request._post['url']
        yt = YouTube(url, on_progress_callback=on_progress)
        formattedViews='{:,}'.format(yt.views)
        Views=yt.views
        lengthh=str(datetime.timedelta(seconds=yt.length))
        thumbnail_url=yt.thumbnail_url
        title=yt.title
        pubdate=yt.publish_date
        channel_name= yt.author
        description=yt.description
        requestdate = date.today()
        

        downlerd = yt.streams.get_highest_resolution()


        
        # We then want to return the web page
    video = Video.objects.create(url=url,Views=Views,description=description,lengthh=lengthh,title=title,pubdate=pubdate,channel_name=channel_name,requestdate=requestdate)
        
    return render(request, "downloader/detail.html", {"channel_name":channel_name,"yt":yt,"formattedViews":formattedViews,"lengthh":lengthh,"thumbnail_url":thumbnail_url,"title":title,"pubdate":pubdate,"description":description, "pk": video.pk})
    
def download_video(request, video_pk):
    video = Video.objects.get(pk=video_pk)
    yt = YouTube(video.url, on_progress_callback=on_progress)
    title=yt.title
    downlerd = yt.streams.get_highest_resolution()
    downlerd.download()
    filename = title + ".mp4"
    file_path = os.path.join(filename)
    return FileResponse(open(file_path, 'rb'), filename=filename, as_attachment=True)

def download_audio(request, video_pk):
    video = Video.objects.get(pk=video_pk)
    yt = YouTube(video.url, on_progress_callback=on_progress)
    title=yt.title
    downlerd=yt.streams.get_audio_only()
    downlerd.download()
    filename=title + ".M4a"

    file_path = os.path.join(filename)
    return FileResponse(open(file_path, 'rb'), filename=filename, as_attachment=True)

