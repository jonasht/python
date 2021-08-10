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


class Principal:
    def __init__(self, tempo=.1):
        self.__tempo = tempo
        
        self.a = auroGame(largura=200, altura=10, background=' ')
        self.nomesObjetos = list(range(60))
        shuffle(self.nomesObjetos)


        for i, nome in enumerate(self.nomesObjetos):
            if len(str(nome)) == 1:
                self.a.set_objeto((' ' + str(nome)), x=i+i+i, y=-5, inicio=bgblue+Fore.WHITE, fim=fim)
            else:   
                self.a.set_objeto(nome, x=i+i+i, y=-5, inicio=bgblue+Fore.WHITE, fim=fim)
            self.a.mostrar()



        self.guardarNumero = 0
    
        self.a.mostrar()
        self.Maneira()
        
    def paraFrente(self, nome2, nome1):
        nome2 = str(nome2)
        nome1 = str(nome1)
        

        if len(nome2) == 1:
            nome2 = ' ' + nome2
        if len(nome1) == 1:
            nome1 = ' ' + nome1
        self.a.reset_objeto(nome=nome1, inicio=bggreen+fgblack)
        self.a.reset_objeto(nome=nome2, inicio=bggreen+fgblack)
        self.a.mostrar()
        sleep(self.__tempo)

        for _ in range(3):
            self.a.move(nome2, op='^')
            self.a.move(nome=nome1, op='v')
            self.a.mostrar()
            sleep(self.__tempo)

        for _ in range(3):
            self.a.move(nome=nome2, op='<')
            self.a.move(nome=nome1, op='>')
            self.a.mostrar()
            sleep(self.__tempo)
            
        for _ in range(3):
            self.a.move(nome=nome2, op='v')
            self.a.move(nome=nome1, op='^')
            self.a.mostrar()
            sleep(self.__tempo)

        self.a.reset_objeto(nome=nome1, inicio=bgblue+fgwhite)
        self.a.reset_objeto(nome=nome2, inicio=bgblue+fgwhite)
        self.a.mostrar()
        sleep(self.__tempo)
    
    
    def Maneira(self):
        for c in np.arange(len(self.nomesObjetos)):
            for i, nomeNum in enumerate(self.nomesObjetos):

                if i+1 == len(self.nomesObjetos):
                    continue
                else:
                    if self.nomesObjetos[i] > self.nomesObjetos[i+1]:
                        self.guardarNumero = self.nomesObjetos[i]
                        self.nomesObjetos[i] = self.nomesObjetos[i+1]
                        self.nomesObjetos[i+1] = self.guardarNumero
                        self.paraFrente(self.nomesObjetos[i], self.nomesObjetos[i+1])


if __name__ == '__main__':

    root = Principal(tempo=0)