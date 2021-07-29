from typing import final
from auro import auroGame
from time import sleep
from colorama.ansi import Back, Fore, Style
from random import shuffle

bgred = Back.RED
bggreen = Back.GREEN
bgblue = Back.BLUE
bgyellow = Back.YELLOW
bgwhite = Back.WHITE
bgblack= Back.BLACK
fim = Style.NORMAL


a = auroGame(largura=50, altura=10, background='  ')
nomesObjetos = list(range(11, 60))
shuffle(nomesObjetos)

for i, nome in enumerate(nomesObjetos):
    a.set_objeto(nome, x=i, y=-5, inicio=bgblue, fim=fim)
    a.mostrar()



guardarNumero = 0
def paraFrente(nome2, nome1, tempo=0.01):
    
    a.mostrar()
    sleep(tempo)
    a.move(nome=nome2, op='up')          
    a.mostrar()
    sleep(tempo)
    a.move(nome=nome1, op='>')
    a.mostrar()
    a.move(nome2, op='left')
    a.mostrar()
    sleep(tempo)
    a.move(nome2, op='down')
    a.mostrar()
    
def Maneira():
    for c in range(len(nomesObjetos)):
        for i in range(len(nomesObjetos)):

            if i+1 == len(nomesObjetos):
                continue
            else:
                if nomesObjetos[i] > nomesObjetos[i+1]:
                    guardarNumero = nomesObjetos[i]
                    nomesObjetos[i] = nomesObjetos[i+1]
                    nomesObjetos[i+1] = guardarNumero
                    paraFrente(nomesObjetos[i], nomesObjetos[i+1])
            a.mostrar()
            # print(nomesObjetos)
Maneira()
# paraFrente('1', '2')
