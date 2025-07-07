import datetime #imports datetime for getting the video length 
from pytubefix import YouTube #imports pytube
from pytubefix.cli import on_progress #grabs on_progress


url = input("url: ")

yt = YouTube(url, on_progress_callback=on_progress) #the video

formattedViews= '{:,}'.format(yt.views) #formatted youtube views

lengthh=str(datetime.timedelta(seconds=yt.length)) #using datetime to turn the amount of seconds in the video to hours:mins:seconds

print(yt.thumbnail_url) #getting the thumbnail of the videos URL

print(yt.title) #a way to print the title

print(f"published on {yt.publish_date} by {yt.channel_url}") #get the publish date of the video and the channel URL

print("\033[4mDescription\033[0m")
print(yt.description) #get the description of the video

downlerd = yt.streams.get_highest_resolution() #get the highest resolution of the video possible

downlerd.download() #download the video

