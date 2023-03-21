from pytube import YouTube



def download_yt(link):
    youtubeObject = YouTube(link)
    # youtubeObject = youtubeObject.streams.get_highest_resolution()
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    
    try:
        youtubeObject.download()
    except:
        return False
    return True


if __name__ == '__main__':
    link = 'https://www.youtube.com/watch?v=vq8ve-5Gu3A'
    link = 'https://www.youtube.com/watch?v=WNeLUngb-Xg'