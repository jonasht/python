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
        
a = auro(20, 10, '0 ')
a.mostrar()
print('----------------------------------------')
a.desenhar('  ', x=5, y=2, qtdCasas= 5 )
a.mostrar()