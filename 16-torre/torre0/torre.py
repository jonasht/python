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
    sleep(0.5)
    system('clear')

a = auro(40, 10, f'{black}  {fim}')

   # Y
   # |
   # |
# ---|----X
   # |

# partes 
parte3 = 20

magica()
a.mostrar()
a.desenhar(f'{blue}  {fim}', x=5 + parte3, y=9, qtdCasas= 9 )
magica()
a.mostrar()
a.desenhar(f'{red}  {fim}', x=6 + parte3, y=8, qtdCasas=7)
magica()
a.mostrar()
a.desenhar(f'{yellow}  {fim}', x=7 + parte3, y=7, qtdCasas=5)
magica()
a.mostrar()
a.desenhar(f'{green}  {fim}', x=8 + parte3, y=6, qtdCasas=3)
magica()
a.mostrar()

