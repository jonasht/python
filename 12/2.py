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

x = y = 0

tamanhaDeX = 10
tamanhaDeY = 10
def mostrar():
    global x
    global y

    print('\n')
    system('clear')
    for i in range(tamanhaDeX):
        for l in range(tamanhaDeY):
            if i == x and l == y:
                print(f'{bgYellow} {f}', flush=True, end='')
            else:
                print(f'{bgBlue} {f}', flush=True, end='')
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


keyboard.wait()
