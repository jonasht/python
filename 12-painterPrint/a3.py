import keyboard
from os import system

black = '\033[30m' # black
red = '\033[31m' # red
green = '\033[32m' # green
yellow = '\033[33m' # yellow
blue = '\033[34m' # blue
magenta = '\033[35m' #
cyan = '\033[36m' #
white = '\033[37m' #
f = '\33[m'

bgBlack = '\033[40m' # background black
bgRed = '\033[41m' # background red
bgGreen = '\033[42m' # background green
bgYellow = '\033[43m' # background yellow
bgBlue = '\033[44m' # background blue
bgMagenta = '\033[45m' # background magenta
bgCyan = '\033[46m' # backgournd cyan
bgWhite = '\033[47m' # backgroundwhite

x = y = 0

tamanhaDeX = 30
tamanhaDeY = 20
picss = list(list(bgWhite+'  ' + f for i in range(tamanhaDeX+ 1))for ii in range(tamanhaDeY + 1))

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
    print(f'{bgBlack+white} 1 {bgRed+black} 2 {bgGreen} 3 {bgYellow} 4 {bgBlue} 5 {bgMagenta} 6 {bgCyan} 7 {bgWhite} 0 {f}')
    for i, pics in enumerate(picss):
        for l, pic in enumerate(pics):
            if i == x and l == y:
                print(f'{bgWhite+corDeLapis}><', flush=True, end='')
            else:
                print(f'{pic}', flush=True, end='')
        print()
    print(f)

mostrar()
def up():
    global x
    if x == 0:
        x = (tamanhaDeX - 1)
    else:
        x -= 1
    mostrar()

def down():
    global x
    if x == tamanhaDeY:
        x = 0
    else:
        x += 1
    mostrar()

def left():
    global y
    if y == 0:
        y = tamanhaDeY
    else:
        y -= 1
    mostrar()

def right():
    global y
    if y == tamanhaDeX:
        y = 0
    else:
        y += 1
    mostrar()

def space():
    global corDePrint
    picss[x][y] = corDePrint + '  ' + f
    mostrar()
    
    
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# cores de lapis

def lapis1(): # pretoblack
    global corDeLapis
    global corDePrint
    corDeLapis = bgBlack
    corDePrint = bgBlack
    mostrar()
    
def lapis2(): # vermelho red
    global corDeLapis
    global corDePrint
    corDeLapis = bgRed
    corDePrint = bgRed
    mostrar()    
    
def lapis3(): # verde green
    global corDeLapis
    global corDePrint
    corDeLapis = bgGreen
    corDePrint = bgGreen
    mostrar()
def lapis4(): #  amarelo yellow
    global corDeLapis
    global corDePrint
    corDeLapis = bgYellow
    corDePrint = bgYellow
    mostrar()
    
def lapis5(): #  azul blue
    global corDeLapis
    global corDePrint
    corDeLapis = bgBlue
    corDePrint = bgBlue
    mostrar()

def lapis6(): #  magenta
    global corDeLapis
    global corDePrint
    corDeLapis = bgMagenta
    corDePrint = bgMagenta
    mostrar()  
    
def lapis7(): #  ciano Cyan
    global corDeLapis
    global corDePrint
    corDeLapis = bgCyan
    corDePrint = bgCyan
    mostrar()      
    
def lapis0(): #  branco
    global corDeLapis
    global corDePrint
    corDeLapis = bgWhite
    corDePrint = bgWhite
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
keyboard.add_hotkey('5', lapis5)
keyboard.add_hotkey('6', lapis6)
keyboard.add_hotkey('7', lapis7)
keyboard.add_hotkey('0', lapis0)

keyboard.add_hotkey('space', space)



keyboard.wait('ESC')
print()
