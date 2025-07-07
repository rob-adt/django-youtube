from django.shortcuts import render
import datetime #imports datetime for getting the video length 
from pytubefix import YouTube #imports pytube
from pytubefix.cli import on_progress #grabs on_progress
from django.http import HttpResponse
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
        lengthh=str(datetime.timedelta(seconds=yt.length))
        thumbnail_url=yt.thumbnail_url
        title=yt.title
        pubdate=yt.publish_date
        channel_name= yt.author
        description=yt.description
        
        # downlerd = yt.streams.get_highest_resolution()
        # downlerd.download()

        # We then want to return the web page
        
        return render(request, "downloader/detail.html", {"channel_name":channel_name,"yt":yt,"formattedViews":formattedViews,"lengthh":lengthh,"thumbnail_url":thumbnail_url,"title":title,"pubdate":pubdate,"description":description})
    
