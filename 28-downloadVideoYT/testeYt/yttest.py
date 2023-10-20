# https://www.youtube.com/watch?v=_p2NvO6KrBs



from pytube import YouTube



yt = YouTube('https://www.youtube.com/watch?v=_p2NvO6KrBs')
print('yt.title:', yt.title)
print('yt.thumbnail_url:', yt.thumbnail_url)
print('stream:', yt.streams)