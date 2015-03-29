from pytube import YouTube
yt = YouTube()
yt.url = 'some_youtube_url'
yt.filename = 'duder'
video = yt.get('mp4', '720p')
video = yt.get('mp4')
import os
os.mkdir(yt.filename)
video.download('/{0}/'.format(yt.filename))
