from auro import auroGame
from time import sleep
from colorama.ansi import Back, Fore, Style
from random import shuffle
import numpy as np

bgred = Back.RED
bggreen = Back.GREEN
bgblue = Back.BLUE
bgyellow = Back.YELLOW
bgwhite = Back.WHITE
bgblack= Back.BLACK
bgcyan = Back.CYAN
bgmagenta = Back.MAGENTA
bgfim = Back.RESET

fgred = Fore.RED
fggreen = Fore.GREEN
fgblue = Fore.BLUE
fgyellow = Fore.YELLOW
fgwhite = Fore.WHITE
fgblack = Fore.BLACK
fgcyan = Fore.CYAN
fgmagenta = Fore.MAGENTA
fgfim = Fore.RESET

fim = Style.NORMAL



a = auroGame(largura=180, altura=10, background=' ')
nomesObjetos = list(range(60))
shuffle(nomesObjetos)


for i, nome in enumerate(nomesObjetos):
    if len(str(nome)) == 1:
        a.set_objeto((' ' + str(nome)), x=i+i+i, y=-5, inicio=bgblue+Fore.WHITE, fim=fim)
    else:   
        a.set_objeto(nome, x=i+i+i, y=-5, inicio=bgblue, fim=fim)
    a.mostrar()



guardarNumero = 0
def paraFrente(nome2, nome1, tempo=0.001):
    nome2 = str(nome2)
    nome1 = str(nome1)
    

    if len(nome2) == 1:
        nome2 = ' ' + nome2
    if len(nome1) == 1:
        nome1 = ' ' + nome1
    a.reset_objeto(nome=nome1, inicio=bggreen+fgblack)
    a.reset_objeto(nome=nome2, inicio=bggreen+fgblack)
    a.mostrar()
    sleep(tempo)

    for _ in range(3):
        a.move(nome2, op='^')
        a.move(nome=nome1, op='v')
        a.mostrar()
        sleep(tempo)

    for _ in range(3):
        a.move(nome=nome2, op='<')
        a.move(nome=nome1, op='>')
        a.mostrar()
        sleep(tempo)
        
    for _ in range(3):
        a.move(nome=nome2, op='v')
        a.move(nome=nome1, op='^')
        a.mostrar()
        sleep(tempo)

    a.reset_objeto(nome=nome1, inicio=bgblue+fgwhite)
    a.reset_objeto(nome=nome2, inicio=bgblue+fgwhite)
    a.mostrar()
    sleep(tempo)
    
def Maneira():
    for c in np.arange(len(nomesObjetos)):
        for i, nomeNum in enumerate(nomesObjetos):

            if i+1 == len(nomesObjetos):
                continue
            else:
                if nomesObjetos[i] > nomesObjetos[i+1]:
                    guardarNumero = nomesObjetos[i]
                    nomesObjetos[i] = nomesObjetos[i+1]
                    nomesObjetos[i+1] = guardarNumero
                    paraFrente(nomesObjetos[i], nomesObjetos[i+1])

a.mostrar()
Maneira()
# paraFrente(' 1', ' 0', 2)
