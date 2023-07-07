


from pytube import YouTube



url=input(" enter url ")

path=""

#for high quality
pytube.YouTube(url).streams.get_highest_resolution().download(path)

#for low quality
pytube.YouTube(url).streams.get_lowest_resolution().download(path)

# just for voice
pytube.YouTube(url).streams.get_audio_only().download(path)

