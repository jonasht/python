import keyboard
from os import system

red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red

select = 0

def mostrar():
    global select

    print('\n')
    system('clear')
    for i in range(5):
        if i == select:
            print(f'{i}|{bgYellow} {f}')
        else:
            print(f'{i}|{bgBlue} {f}')


def up():
    global select
    if select == 0:
        return
    select -= 1
    mostrar()

def down():
    global select
    if select == 4:
        return
    select += 1
    mostrar()


keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('w', up)
keyboard.add_hotkey('s', down)


keyboard.wait()
