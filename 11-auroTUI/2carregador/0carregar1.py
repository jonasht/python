from time import sleep
from os import system

def carregador():
    sleep(.5)
    for i in range(51):
        print(f'[{(i*2):<3}%] [{("#" * i):>}{("." * (51-i-1))}]', flush=True)
        
        sleep(.03)
        
        system('clear')
    print()
carregador()