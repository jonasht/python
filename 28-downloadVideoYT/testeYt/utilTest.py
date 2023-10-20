import urllib.request

def download_image(thumbnail_url:str, name:str) -> None:
    path = f'./video_image/{name}.jpg'
    urllib.request.urlretrieve(thumbnail_url, path)



