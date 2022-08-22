# auroGame versão 2 dev 
# versão 2: arrumado o bug de move() right

from time import sleep
from os import system
import numpy as np
from colorama.ansi import Back, Fore, Style 

class auroGame:
    def __init__(self, largura, altura, background=0):
        self.largura = largura
        self.altura = altura
        self.background = background+Back.RESET
        self.desenho = [[self.background for _ in np.arange(self.largura)] for _ in np.arange(self.altura)]
        self.posicao = {}
        self.info = {}
    
    
    # desenhar na tela 
    def desenhar(self, nome, x=2, y=2, qtdCasas=2, ):
        for i in np.arange(qtdCasas):
            self.desenho[y][x+i] = nome
    
    # definir objeto
    def set_objeto(self, nome, x, y, qtdCasas=0, inicio='', fim=Style.NORMAL):
        nome = str(nome)
        qtdCasas = int(qtdCasas)
        fim = Back.RESET if fim else ''
        
        if qtdCasas == 0:
            for i, n in enumerate(nome):
                self.desenho[y][x+i] = str(inicio+n+fim)
            
        else:
            for i in np.arange(qtdCasas):
                
                self.desenho[y][x+i] = str(inicio+nome+fim)

        posicao = {'nome': nome, 'x': x, 'y': y, 'qtdCasas': qtdCasas, 'inicio': inicio, 'fim': fim}
        self.set_posicao(posicao)
        
    # re configura objeto
    def reset_objeto(self, nome, x=None, y=None, qtdCasas=None, inicio=None, fim=None):
        nome = str(nome)

        if x:
            self.posicao[nome]['x'] = int(x)
        if y:
            self.posicao[nome]['y'] = int(y)
        if qtdCasas:
            self.posicao[nome]['qtdCasas'] = int(qtdCasas)
        if inicio:
            self.posicao[nome]['inicio'] = inicio
        if fim:
            self.posicao[nome]['fim'] = fim

        x = self.posicao[nome]['x']
        y = self.posicao[nome]['y']
        
        
        qtdCasas = self.posicao[nome]['qtdCasas']
        inicio = self.posicao[nome]['inicio']
        fim = self.posicao[nome]['fim']

        if self.posicao[nome]['qtdCasas'] == 0:
            for i, n in enumerate(nome):
                self.desenho[y][x+i] = inicio+n+fim
        else:
            for i in np.arange(qtdCasas):
                self.desenho[y][x+i] = inicio+nome+fim

    # mover 
    def move(self, nome, op='>'):
        nome = str(nome)
        
        posicao = self.posicao[nome]
        
        if posicao['qtdCasas'] == 0:
            qtdCasas = len(nome)
        else: 
            qtdCasas = posicao['qtdCasas']

        if op == '>' or op == 'right':
            self.set_objeto(posicao['nome'], posicao['x']+1, posicao['y'], posicao['qtdCasas'],
                            posicao['inicio'], posicao['fim']) 
                       
            self.remove(posicao['x'], posicao['y'], 1)
            
        if op == '<' or op.lower() == 'left':
            self.set_objeto(posicao['nome'], posicao['x']-1, posicao['y'], posicao['qtdCasas'],
                            posicao['inicio'], posicao['fim'])

            self.remove(posicao['x']+qtdCasas-1, posicao['y'], 1)
        
        if op == '^' or op.lower() == 'up':
            self.set_objeto(posicao['nome'], posicao['x'], posicao['y']-1, posicao['qtdCasas'],
                            posicao['inicio'], posicao['fim'])
            
            self.remove(posicao['x'], posicao['y'], qtdCasas)

        if op.lower() == 'v' or op.lower() == 'down':
            self.set_objeto(posicao['nome'], posicao['x'], posicao['y']+1, posicao['qtdCasas'],
                            posicao['inicio'], posicao['fim'])
            
            self.remove(posicao['x'], posicao['y'], qtdCasas)


    def remove(self, x, y, qtdCasas):
        
        for i in range(qtdCasas):
            self.desenho[y][x+i] = self.background
        
    def set_info(self, **usar_info):
        
        for k, v in usar_info.items():
            self.info[k] = v
    
    def get_info(self):
        return self.info

    # mostrar desenho 
    def mostrar(self):
        system('clear')
        # for chars in self.desenho:
        #     for char in chars:
        #         print(f'{char}', end='')
        #     print()
        
        # fazendo de outro jeito
        
        screen = ''
        for line in self.desenho:
            screen += ''.join(line) + '\n'
        
        # monstrando desenho na tela
        print(screen)
            

    
    # apagar desenho 
    def apagar(self, x, y, qtdCasas):
        self.desenho[y][x] = self.background
    
    def set_posicao(self, p): 
        # p é de posicao
       self.posicao[p['nome']] = {
           'nome': p['nome'], 
           'x': p['x'], 
           'y': p['y'],
           'qtdCasas': p['qtdCasas'],
           'inicio': p['inicio'],
           'fim': p['fim']
           }

    def get_posicao(self):
        return self.posicao

# fazendo teste ou demostrando 
if __name__ == '__main__':
    fim = '\033[0m'
    black = '\033[40m ' + fim  
    red = '\033[41m.'  + fim
    green = '\033[42m ' + fim
    yellow = '\033[43m ' + fim
    blue = '\033[44m ' + fim 
    pink = '\033[45m ' + fim 
    white = '\033[107m ' + fim 

    def mostrar(tempo=.05):
        sleep(tempo)
        a.mostrar()

    a = auroGame(50, 11, ' ')
    a.mostrar()

    # definindo o objeto ou nome para movimentar
    objeto = red
    
    a.set_objeto(objeto, x=20, y=5, qtdCasas=3)
    
    # desenhando
    a.desenhar(white, 19, 6, 10)
    a.desenhar(white, 20, 4, 10)
    a.mostrar()

    for i in range(5):
        for _ in range(2):

            for _ in range(1+i):
                a.move(objeto, '<')
                mostrar()

            for _ in range(3):
                a.move(objeto, '^')
                mostrar()
                
            for _ in range(1):
                a.move(objeto, '>')
                mostrar()
                
            for _ in range(2):
                a.move(objeto, 'v')
                mostrar()

