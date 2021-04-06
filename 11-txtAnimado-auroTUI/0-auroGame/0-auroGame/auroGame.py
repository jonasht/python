# auroGame versão 0 dev - de: versão auroDesenhante 5 dev

from time import sleep
from os import system

class auro:
    def __init__(self, largura, altura, background=0):
        self.largura = largura
        self.altura = altura
        self.background = background
        self.desenho = [[self.background for ii in range(self.largura)] for i in range(self.altura)]
        self.posicao = {}
        self.info = {}
    
    
    # desenhar na tela 
    def desenhar(self, nome, x=2, y=2, qtdCasas=2, ):
        for i in range(qtdCasas):
            self.desenho[y][x+i] = nome
    
    # definir objeto
    def set_objeto(self, nome, x, y, qtdCasas, ):
        for i in range(qtdCasas):
            self.desenho[y][x+i] = nome
        posicao = {'nome': nome, 'x': x, 'y': y, 'qtdCasas': qtdCasas}
        self.set_posicao(posicao)
        
    # mover 
    def move(self, nome, op='>'):

        posicao = self.posicao[nome]

        if op == '>' or op == 'right':
            self.set_objeto(posicao['nome'], posicao['x']+1, posicao['y'], posicao['qtdCasas'])
            self.remove(posicao['x'], posicao['y'], posicao['qtdCasas'])
            
        if op == '<' or op.lower() == 'left':
            self.set_objeto(posicao['nome'], posicao['x']-1, posicao['y'], posicao['qtdCasas'])
            self.remove(posicao['x'], posicao['y'], posicao['qtdCasas'])
        
        if op == '^' or op.lower() == 'up':
            self.set_objeto(posicao['nome'], posicao['x'], posicao['y']-1, posicao['qtdCasas'])
            self.remove(posicao['x'], posicao['y'], posicao['qtdCasas'])

        if op.lower() == 'v' or op.lower() == 'down':
            self.set_objeto(posicao['nome'], posicao['x'], posicao['y']+1, posicao['qtdCasas'])
            self.remove(posicao['x'], posicao['y'], posicao['qtdCasas'])


    def remove(self, x, y, qtdCasas):
        for i in range(qtdCasas):
            self.desenho[y][x+i] = self.background
        
    def set_info(self, **info):
        self.info = info
    
    def get_info(self):
        return self.info

    # mostrar desenho 
    def mostrar(self):
        system('clear')
        for chars in self.desenho:
            for char in chars:
                print(f'{char}', end='')
            print()
            
    
    # apagar desenho 
    def apagar(self, x, y, qtdCasas):
        self.desenho[y][x] = self.background
    
    def set_posicao(self, p): 
        # p é de posicao
       self.posicao[p['nome']] = {
           'nome': p['nome'], 
           'x': p['x'], 
           'y': p['y'],
           'qtdCasas': p['qtdCasas']}
    
    def get_posicao(self):
        return self.posicao

if __name__ == '__main__':
    fim = '\033[0m'
    black = '\033[40m ' + fim  
    red = '\033[41m '  + fim
    green = '\033[42m ' + fim
    yellow = '\033[43m ' + fim
    blue = '\033[44m ' + fim 
    pink = '\033[45m ' + fim 
    white = '\033[107m ' + fim 
    def mostrar():
        sleep(.2)
        a.mostrar()

    a = auro(50, 11, ' ')
    a.mostrar()

    # definindo o objeto ou nome para movimentar
    objeto = red
    a.set_objeto(objeto, x=20, y=5, qtdCasas=1)
    a.desenhar(white, 19, 6, 5)
    a.desenhar(white, 20, 4, 5)
    a.mostrar()


    for _ in range(2):
        for _ in range(3):
            a.move(objeto, '>')
            mostrar()

        for _ in range(5):
            a.move(objeto, '<')
            mostrar()
        a.move(objeto, '^')
        mostrar()
        for _ in range(3):
            a.move(objeto, '>')
            mostrar()
        for _ in range(3):
            a.move(objeto, 'v')
            mostrar()

