from auroDesenhante import *

fim = '\033[0m'
black = '\033[40m'
red = '\033[41m' 
green = '\033[42m'
yellow = '\033[43m'
blue = '\033[44m'
pink = '\033[45m'
white = '\033[107m'



def magica():
    sleep(0.2)
    system('clear')


   # Y
   # |
   # |
# ---|----X
   # |

# a = auro(40, 10, f'{black}  {fim}')
# partes 
parte3 = 20

# magica()
# a.mostrar()
# a.desenhar(f'{blue}  {fim}', x=5 + parte3, y=9, qtdCasas= 9 )
# magica()
# a.mostrar()
# a.desenhar(f'{red}  {fim}', x=6 + parte3, y=8, qtdCasas=7)
# magica()
# a.mostrar()
# a.desenhar(f'{yellow}  {fim}', x=7 + parte3, y=7, qtdCasas=5)
# magica()
# a.mostrar()
# a.desenhar(f'{green}  {fim}', x=8 + parte3, y=6, qtdCasas=3)
# magica()
# a.mostrar()

def erguer(nomeBarra, x, y, qtdCasas, erguerAte=5):
   ry = 0
   for i in range(1, erguerAte):
      
      backend.desenhar(nomeBarra, x, y-i, qtdCasas)
      backend.apagar(x, y-i+1, qtdCasas)
      backend.mostrar()
      magica()
      ry = y-1
   # print('X: ', x, 'Y: ', ry )
   return nomeBarra, x, ry, qtdCasas
      
         

def baixar():
   pass

def movimentar(nomeBarra, x, y, qtdCasas, moveAte = 5):
   pass

magica()
backend = auro(40, 10, f' ') 
backend.mostrar()

backend.desenhar(f'4', x=5 + parte3, y=9, qtdCasas= 9 )
magica()
backend.mostrar()
backend.desenhar(f'3', x=6 + parte3, y=8, qtdCasas=7)
magica()
backend.mostrar()
backend.desenhar(f'2', x=7 + parte3, y=7, qtdCasas=5)
magica()
backend.mostrar()
backend.desenhar('1', x=8 + parte3, y=6, qtdCasas=3)
magica()
backend.mostrar()

magica()
rnomeBarra, rx, ry, rqtdCasas = erguer('1', x=8 + parte3, y=6, qtdCasas=3)
backend.mostrar()
