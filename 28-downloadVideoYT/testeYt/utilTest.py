import urllib.request

def download_image(thumbnail_url:str, name:str) -> None:
    path = f'./video_image/{name}.jpg'
    urllib.request.urlretrieve(thumbnail_url, path)



def format_bytes(size:int) ->str:
    # 2**10 = 1024
    power = 2**10
    n = 0
    # power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    power_labels = {0 : '', 1: 'kilo', 2: 'mg', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    # return size, power_labels[n]+'bytes'
    return f'{size:.0f}{power_labels[n]}' 
    
if __name__ == '__main__':
    size = 17408912
    print(format_bytes(size))