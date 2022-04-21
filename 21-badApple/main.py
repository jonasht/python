from time import sleep, time
from os import system
import playsound
import uteis as u
from colorama import Fore


def main():
    frames = u.load('./assets/frames0.txt')

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
            # print(frame)
            print(f'{frame}frame:{i}|{frames_size}', end='')
            sleep(sleep_time)

        

if __name__ == '__main__':
    main()