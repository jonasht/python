from pytube import YouTube
import urllib.request

link = 'https://www.youtube.com/watch?v=_p2NvO6KrBs'
def download_image(thumbnail_url:str, name:str) -> None:
    path = f'./video_image/{name}.jpg'
    urllib.request.urlretrieve(thumbnail_url, path)


yt = YouTube(link)
thumbnail_url = yt.thumbnail_url
print(yt.title)
download_image(thumbnail_url=thumbnail_url, name=yt.title)

