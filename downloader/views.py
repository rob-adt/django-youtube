# views.py
from django.shortcuts import render
import datetime
from pytubefix import YouTube
from pytubefix.cli import on_progress
from django.http import HttpResponse, FileResponse
from .models import Video, Request
from datetime import date
import time
import os
from moviepy import CompositeAudioClip, VideoFileClip, AudioFileClip, CompositeVideoClip

temp_folder = "tmp/"

def index(request):
    if request.method == 'GET':
        return render(request, "downloader/index.html")
    elif request.method == 'POST':
        url = request.POST.get('url')
        yt = YouTube(url, on_progress_callback=on_progress)
        formattedViews = '{:,}'.format(yt.views)
        Views = yt.views
        lengthh = str(datetime.timedelta(seconds=yt.length))
        thumbnail_url = yt.thumbnail_url
        title = yt.title or 'Default Title'  # Provide a default title if not available
        pubdate = yt.publish_date
        channel_name = yt.author
        description = yt.description
        requestdate = date.today()
        timereq = time.strftime("%H:%M:%S", time.localtime())
        stringdate = f"Request on {requestdate} {timereq}"

        downlerd = yt.streams.get_highest_resolution()





        video, created = Video.objects.get_or_create(url=url,lengthh=lengthh,pubdate=pubdate,defaults={'title': title,'Views': Views,'description': description,'channel_name': channel_name,'timereq': timereq,'requestdate': requestdate})

        request = Request.objects.create(title=title,requestdate=requestdate,channel_name=channel_name,stringdate=stringdate,timereq=timereq,url=url,keys=video)

        

        return render(request, "downloader/detail.html", {"channel_name": channel_name,"yt": yt,"formattedViews": formattedViews,"lengthh": lengthh,"thumbnail_url": thumbnail_url,"title": title,"pubdate": pubdate,"description": description,"pk": video.pk})

def download_video(request, video_pk):
    video = Video.objects.get(pk=video_pk)
    yt = YouTube(video.url, on_progress_callback=on_progress)
    title = yt.title
    # Get the highest resolution video stream (without audio)
    video_stream = yt.streams.filter(file_extension="mp4", only_video=True,res=["1440p","1080p", "720p", "360p", "240p", "144p"]).order_by('resolution').desc().first()

    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    if not video_stream or not audio_stream:
            raise Exception('No suitable video or audio streams found.')

    # Log the resolution and audio quality
    print(f"Downloading video in resolution: {video_stream.resolution}")
    print(f"Downloading audio with bitrate: {audio_stream.abr}")

    # Download video and audio streams
    video_path = video_stream.download(output_path=temp_folder, filename="video.mp4", )
    audio_path = audio_stream.download(output_path=temp_folder, filename="audio.mp3")  
    videoclip = VideoFileClip("tmp/video.mp4")
    audioclip = AudioFileClip("tmp/audio.mp3")

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("tmp/combined_video.mp4") 
    filename = title + ".mp4"
    file_path = os.path.join(filename)
    return FileResponse(open("tmp/combined_video.mp4", 'rb'), filename=filename, as_attachment=True)

def download_audio(request, video_pk):
    video = Video.objects.get(pk=video_pk)
    yt = YouTube(video.url, on_progress_callback=on_progress)
    title = yt.title
    downlerd = yt.streams.get_audio_only()
    downlerd.download()
    filename = title + ".M4a"
    file_path = os.path.join(filename)
    return FileResponse(open(file_path, 'rb'), filename=filename, as_attachment=True)
