from time import sleep
from os import system



for i in range(101):
    print(f'       !{str(i):>3}%')
    sleep(.09)
    system('clear')