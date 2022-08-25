from time import sleep
from random import shuffle
from os import system
import colorama
from colorama.ansi import Back
import numpy as np
colorama.init()


class Interface:
    def __init__(self):
        self.f = '\33[1;0m'

        # self.bgblack = '\033[1;40m' # background black
        # self.bggreen = '\033[1;42m' # background green
        # self.bgBlue = '\033[1;44m'  # backgournd blue
        # self.bgYellow = '\033[1;43m'# backgournd yellow
        # self.bgRed = '\033[1;41m'   # backgournd red
        # self.bgwhite = '\033[1;107m'# background white
        
        self.bgblack = Back.BLACK
        self.bggreen = Back.GREEN
        self.bgBlue = Back.BLUE
        self.bgYellow = Back.YELLOW
        self.bgRed = Back.RED
        self.bgwhite = Back.WHITE 
        
        
        
        
        
    def set_tamanhoDaLista(self, tamanho):
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definição do tamanho da lista
        self.tamanhoDaLista = tamanho
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        # embaralhanto a lista 
        self.lista = list(np.arange(1, self.tamanhoDaLista))

        shuffle(self.lista)
        
    def set_tempoDeAtraso(self, tempoDeAtraso):
        # definir o tempo de atraso
        self.tempoDeAtraso = tempoDeAtraso

    def set_charPixel(self, charPixel):
        self.charPixel = charPixel
        
    # mostrar lista, serve para mostrar a lista de forma legal
    def Mostrar(self, mostrarLista, frontend=True):
        system('clear')       

        screen = ''
        if frontend:
            for cs in mostrarLista:
                for c in cs:
                    if c == 1:
                        screen += f'{self.bgBlue}{self.charPixel}{self.f}'
                    elif c == 2:
                        screen += f'{self.bggreen}{self.charPixel}{self.f}'
                    elif c == 3:
                        screen += f'{self.bgYellow}{self.charPixel}{self.f}'

                    else:
                        screen += f'{self.charPixel}'
                screen += '\n'
        else:
            for cs in mostrarLista:
                for c in cs:
                    if c == 1:
                        screen += f'{self.bgBlue} {c} {self.f}'
                    elif c == 2:
                        screen += f'{self.bggreen} {c} {self.f}'
                    elif c == 3:
                        screen += f'{self.bgYellow} {c} {self.f}'
                    else:
                        screen += f'   '
                screen += '\n'
                
        print(screen)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    
        sleep(self.tempoDeAtraso)           
        


    # aqui serve para tranformar uma lista em matriz para mostrar() conseguir mostrar
    def converterPMostrar(self, n, oque):
        
        mostrarLista = [([0 for i in np.arange(self.tamanhoDaLista)]) for i in np.arange(self.tamanhoDaLista)]
        
        
        for contador in np.arange(len(self.lista)):
            for i, chars in enumerate(mostrarLista[::-1]):
                if self.lista[contador] == i: 
                    break        

                chars[contador] = 1
                
                if contador == n:
                    chars[contador] = oque
    
                    
                    
        self.Mostrar(mostrarLista)