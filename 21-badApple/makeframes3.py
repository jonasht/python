from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from typing import Tuple


import cv2
import tqdm
from colorama import Back

from uteis import save
import uteis as u

def draw_frame(frame_information: Tuple[int, cv2.VideoCapture]):
    order, frame = frame_information
    
    y, x, _ = frame.shape
    frame_str = ''
    pixel_row = 0
    
    for this_y in range(y):
        for this_x in range(x):
            pixel = '0' if frame[this_y, this_x].all() == 0 else ' '

            frame_str += pixel
            
            pixel_row += 1
            if pixel_row == x:
                frame_str += '\n'
                pixel_row = 0
    
    return order, frame_str
    

def generate_frames(video: cv2.VideoCapture):
    success = True
    order = 0
    
    while success:
        success, frame = video.read()
        _, bw_frame = cv2.threshold(frame, 128, 255, cv2.THRESH_BINARY)

        if bw_frame is None:
            break
        
        y, x, _ = bw_frame.shape
        bw_frame = cv2.resize(bw_frame, (x // 4, y // 5))
        
        yield order, bw_frame
        
        order += 1

if __name__ == '__main__':
    
    VIDEO_PATH = './assets/badapple.mp4'
    VIDEO = cv2.VideoCapture(VIDEO_PATH)
    VIDEO_FRAMES_COUNT = int(VIDEO.get(cv2.CAP_PROP_FRAME_COUNT))
    
    
    with ThreadPool(processes=cpu_count()) as pool:
        frames = list(tqdm.tqdm(pool.imap(draw_frame, generate_frames(VIDEO)), total=VIDEO_FRAMES_COUNT))
        pool.close()
        pool.join()
        
    frames = sorted(frames, key=lambda x: x[0])
    
    
    prints = list()
    
    for _, frame in frames:
        prints.append(frame)
        
    # save(prints, 'framesVerde.txt')
    # salvando em binario
    for i, print in enumerate(prints):
        u.dumb(print, f'./assets/frames/frame{i}')
    print('funcionou')
