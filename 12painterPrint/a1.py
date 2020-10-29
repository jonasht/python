import keyboard
from os import system

red = '\033[31m' # red
blue = '\033[35m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red
bgGreen = '\033[42m' # background green
bgWhite = '\033[47m' # backgroundwhite

x = y = 0

tamanhaDeX = 15
tamanhaDeY = 10
picss = list(list(bgWhite+'  ' + f for i in range(tamanhaDeX))for ii in range(tamanhaDeY))

corDeLapis = green
corDePrint = bgWhite
def mostrar():
    global x
    global y
    global corDeLapis
    global corDePrint

    system('clear')
    print('\n')
    
    print('space for printing// espaço p pintar')
    print('aperte esc para sair// ESC to exit')
    print(f'{bgRed} 1 {bgGreen} 2 {bgYellow} 3 {bgBlue} 4 {f}'+ f)
    for i, pics in enumerate(picss):
        for l, pic in enumerate(pics):
            if i == x and l == y:
                print(f'{bgWhite+corDeLapis}><', flush=True, end='')
            else:
                print(f'{pic}', flush=True, end='')
        print(f)

mostrar()
def up():
    global x
    if x == 0:
        return
    x -= 1
    mostrar()

def down():
    global x
    if x == tamanhaDeY:
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
    if y == tamanhaDeX:
        return
    y += 1
    mostrar()

def space():
    global corDePrint
    picss[x][y] = corDePrint + '  '
    mostrar()
def lapis1(): # vermelho red
    global corDeLapis
    global corDePrint
    corDeLapis = bgRed
    corDePrint = bgRed
    mostrar()
def lapis2(): # verde green
    global corDeLapis
    global corDePrint
    corDeLapis = bgGreen
    corDePrint = bgGreen
    mostrar()    
def lapis3(): # amarelo yellow
    global corDeLapis
    global corDePrint
    corDeLapis = bgYellow
    corDePrint = bgYellow
    mostrar()
def lapis4(): # azul blue
    global corDeLapis
    global corDePrint
    corDeLapis = bgBlue
    corDePrint = bgBlue
    mostrar()

     
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', right)
keyboard.add_hotkey('left', left)

keyboard.add_hotkey('w', up)
keyboard.add_hotkey('s', down)
keyboard.add_hotkey('d', right)
keyboard.add_hotkey('a', left)

keyboard.add_hotkey('1', lapis1)
keyboard.add_hotkey('2', lapis2)
keyboard.add_hotkey('3', lapis3)
keyboard.add_hotkey('4', lapis4)

keyboard.add_hotkey('space', space)



keyboard.wait('ESC')
