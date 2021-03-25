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
    

fim = '\033[0m'
black = '\033[40m'
red = '\033[41m' 
green = '\033[42m'
yellow = '\033[43m'
blue = '\033[44m'
pink = '\033[45m'
white = '\033[107m'

a = auro(20, 10, f'{black}  {fim}')
a.mostrar()
print('----------------------------------------')
a.desenhar(f'{blue}  {fim}', x=5, y=9, qtdCasas= 9 )
a.mostrar()
a.desenhar(f'{red}  {fim}', x=6, y=8, qtdCasas=7)
a.mostrar()
a.desenhar(f'{yellow}  {fim}', x=7, y=7, qtdCasas=5)
a.mostrar()
a.desenhar(f'{green}  {fim}', x=8, y=6, qtdCasas=3)
a.mostrar()
a.desenhar(f'{white}  {fim}', x=7, y=7, qtdCasas=5)
a.mostrar()