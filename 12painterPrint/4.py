import keyboard
from os import system

red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
white = '\033[37m' # white
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red
bgGreen = '\033[42m' # background green
bgWhite = '\033[47m' # backgroundwhite

x = y = 0

tamanhaDeX = 10
tamanhaDeY = 10
def mostrar():
    global x
    global y


    system('clear')
    print('\n')
    print('aperte esc para sair// ESC to exit')
    print(f'{bgRed+white} 1 {bgGreen+white} 2 {bgYellow+white} 3 {bgBlue+white} 4 {f}')
    for i in range(tamanhaDeX):
        for l in range(tamanhaDeY):
            if i == x and l == y:
                print(f'{bgYellow+green}><{f}', flush=True, end='')
            else:
                print(f'{bgWhite}  {f}', flush=True, end='')
        print()

mostrar()
def up():
    global x
    if x == 0:
        return
    x -= 1
    mostrar()

def down():
    global x
    if x == tamanhaDeX:
        return
    x += 1
    mostrar()

def left():
    global y
    if y == 0:
        return
    y -= 1
    mostrar()

def right():
    global y
    if y == tamanhaDeY:
        return
    y += 1
    mostrar()

keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', right)
keyboard.add_hotkey('left', left)

keyboard.add_hotkey('w', up)
keyboard.add_hotkey('s', down)


keyboard.wait('ESC')
