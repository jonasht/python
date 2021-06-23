# versão 4 dev

from time import sleep
from os import system
class auro:
    def __init__(self, largura, altura, encher=0):
        self.largura = largura
        self.altura = altura
        self.encher = encher
        self.desenho = [[self.encher for ii in range(self.largura)] for i in range(self.altura)]
    
    
    def desenhar(self, comOque, x=2, y=2, qtdCasas=2, ):
        for i in range(qtdCasas):
            self.desenho[y][x+i] = comOque
            
    def mostrar(self):
        for chars in self.desenho:
            for char in chars:
                print(f'{char}', end='')
            print()
    def apagar(self, x, y, qtdCasas):
        for i in range(qtdCasas):
            self.desenho[y][x+i] = self.encher
            

fim = '\033[0m'
black = '\033[40m'
red = '\033[41m' 
green = '\033[42m'
yellow = '\033[43m'
blue = '\033[44m'
pink = '\033[45m'
white = '\033[107m'
