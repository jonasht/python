from auroDesenhante import *


def magica():
    # sleep(0.5)
    sleep(.1)
    system('clear')

def subir(nome):
   info = backend.get_posicao()[nome]
   # for i in range(3):
   backend.desenhar(info['nome'], info['x'], info['y']-1, info['qtdCasas'])
   backend.apagar(info['x'], info['y']-1+1, info['qtdCasas'])
   backend.mostrar()
   print()
   print(info['y']-1)
   print(backend.get_posicao()[nome])
def mover(nome):
   pass

backend = auro(56, 10, f' ')
parte1 = 15
parte2 = 30
parte3 = 45

backend.mostrar()
print('----------------------------------------')
backend.desenhar(f'4', x=parte3, y=9, qtdCasas= 9 )
magica()
backend.mostrar()
backend.desenhar(f'3', x=parte3+1, y=8, qtdCasas=7)
magica()
backend.mostrar()
backend.desenhar(f'2', x=parte3+2, y=7, qtdCasas=5)
magica()
backend.mostrar()
backend.desenhar(f'1', x=parte3+3, y=6, qtdCasas=3)
magica()
backend.mostrar()


print('='*30)
# print(backend.get_posicao()['1'])
subir('1')