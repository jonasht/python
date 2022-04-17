from time import sleep, time
from os import system
import playsound
from uteis import read, str_ToList
from colorama import Fore


def main():
    
    
    frames = read()
    frames = str_ToList(frames)


    FPS = 30
    skip_ticks = 1/(FPS*1.0)
    next_snap = time()
    

    frames_size = len(frames)
    
    playsound.playsound('./assets/badapple.mp3', block=False)
    for i, frame in enumerate(frames):
        system('clear')
        next_snap += skip_ticks
        sleep_time = next_snap - time()
        
        if sleep_time > 0:
            
            # print(f'{Fore.GREEN}{frame}')
            print(frame)
            sleep(sleep_time)
        print(f'frame:{i}|{frames_size}')
        

if __name__ == '__main__':
    main()