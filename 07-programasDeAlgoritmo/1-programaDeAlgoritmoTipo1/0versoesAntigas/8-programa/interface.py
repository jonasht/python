from time import sleep
from random import shuffle
from os import system


class Interface:
    def __init__(self):
        self.f = '\33[1;0m'

        self.bgblack = '\033[1;40m' # background black
        self.bggreen = '\033[1;42m' # background green
        self.bgBlue = '\033[1;44m'  # backgournd blue
        self.bgYellow = '\033[1;43m'# backgournd yellow
        self.bgRed = '\033[1;41m'   # backgournd red
        self.bgwhite = '\033[1;107m'# background white

        
    def set_tamanhoDaLista(self, tamanho):
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definição do tamanho da lista
        self.tamanhoDaLista = tamanho
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        self.lista = list(range(1, self.tamanhoDaLista))

        shuffle(self.lista)
        
    def set_tempoDeAtraso(self, tempoDeAtraso):
        # definir o tempo de atraso
        self.tempoDeAtraso = tempoDeAtraso

    # mostrar lista, serve para mostrar a lista de forma legal
    def Mostrar(self, mostrarLista):
        system('clear')
        for cs in mostrarLista:
            for c in cs:
                if c == 1:
                    print(f'{self.bgBlue}  {self.f}', end='')
                elif c == 2:
                    print(f'{self.bggreen}  {self.f}', end='')
                else:
                    print(f'  ', end='')
            print()
        
        sleep(self.tempoDeAtraso)                  


    # aqui serve para tranformar uma lista em matriz para mostrar() conseguir mostrar
    def converterPMostrar(self, n):
        
        mostrarLista = [([0 for i in range(self.tamanhoDaLista)]) for i in range(self.tamanhoDaLista)]
        
        
        for contador in range(len(self.lista)):
            for i, chars in enumerate(mostrarLista[::-1]):
                if self.lista[contador] == i: break        
                chars[contador] = 1
                
                if contador == n:
                    chars[contador] = 2    
    
                    
                    
        self.Mostrar(mostrarLista)
        mostrarLista.clear()
        #sleep(.02)    


