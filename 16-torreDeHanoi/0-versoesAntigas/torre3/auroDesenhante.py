# versão 5 dev

from time import sleep
from os import system

class auro:
    def __init__(self, largura, altura, encher=0):
        self.largura = largura
        self.altura = altura
        self.encher = encher
        self.desenho = [[self.encher for ii in range(self.largura)] for i in range(self.altura)]
        self.posicao = {}
    
    
    def desenhar(self, comOque, x=2, y=2, qtdCasas=2, ):
        for i in range(qtdCasas):
            self.desenho[y][x+i] = comOque
        posicao = {'nome': comOque, 'x': x, 'y': y, 'qtdCasas': qtdCasas}
        self.set_posicao(posicao)

        
    def mostrar(self):
        for chars in self.desenho:
            for char in chars:
                print(f'{char}', end='')
            print()

    def apagar(self, x, y, qtdCasas):
        for i in range(qtdCasas):
            self.desenho[y][x+i] = self.encher
            
    def set_posicao(self, p): 
        # p é de posicao
       self.posicao[p['nome']] = {
           'nome': p['nome'], 
           'x': p['x'], 
           'y': p['y'],
           'qtdCasas': p['qtdCasas']}
    
    def get_posicao(self):
        return self.posicao
            # 
# fim = '\033[0m'
# black = '\033[40m'
# red = '\033[41m' 
# green = '\033[42m'
# yellow = '\033[43m'
# blue = '\033[44m'
# pink = '\033[45m'
# white = '\033[107m'
# 
# def magica():
    # sleep(0.5)
    # sleep(.1)
    # system('clear')
# 
# a = auro(40, 10, f'{black}  {fim}')
# 
# a.mostrar()
# print('----------------------------------------')
# a.desenhar(f'{blue}  {fim}', x=5, y=9, qtdCasas= 9 )
# magica()
# a.mostrar()
# a.desenhar(f'{red}  {fim}', x=6, y=8, qtdCasas=7)
# magica()
# a.mostrar()
# a.desenhar(f'{yellow}  {fim}', x=7, y=7, qtdCasas=5)
# magica()
# a.mostrar()
# a.desenhar(f'{green}  {fim}', x=8, y=6, qtdCasas=3)
# magica()
# a.mostrar()
# a.desenhar(f'{white}  {fim}', x=7, y=3, qtdCasas=5)
# magica()
# a.mostrar()
# a.apagar(x=7, y=3, qtdCasas=5)
# magica()
# a.mostrar()
# 
# print('-------------------------------------------------------------')
# print('posicao')
# print(a.get_posicao())
# mostrar possicao de modo melhor
# for nome, posicao in a.get_posicao().items():
    # print(f'nomePrimario: {nome} - ', end='')
    # for n, p in posicao.items():
        # print(f'{n}:{p} ', end='')
    # print()