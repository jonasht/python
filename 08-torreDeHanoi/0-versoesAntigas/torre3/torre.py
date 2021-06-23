from auroDesenhante import *

# espacamento entre as barras
# esp = {
#    '1': 3,
#    '2': 2,5,
#    '3': 1,
#    '4': 0,}

def magica():
    # sleep(0.5)
    sleep(.1)
    system('clear')

def up(nome):
   info = backend.get_posicao()[nome]
   for i in range(1, 3):
      backend.desenhar(info['nome'], info['x'], info['y']-i, info['qtdCasas'])
      backend.apagar(info['x'], info['y']-i+1, info['qtdCasas'])
      sleep(.01)
      system('clear')
      backend.mostrar()
   
   # print(info['y']-1)
   # print(backend.get_posicao()[nome])
def move(nome, parte=''):
   info = backend.get_posicao()[nome]
   
   for i in range(1, 15):
      backend.desenhar(info['nome'], info['x']-i, info['y'], info['qtdCasas'])
      backend.apagar(backend.get_posicao()[nome]['x'] + info['qtdCasas'], info['y'], 1)
      
      sleep(.01)
      system('clear')
      backend.mostrar()
      print(info['nome'], 'x:', info['x']-i, 'y:', info['y'], 'qrdCasas:', 'qtdCasas:', info['qtdCasas'])
      # print('apagar: ', 'x:', info['x']+3, 'y:', info['y'], 'qrdCasas:', info['qtdCasas'])
   

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

# up('1')
move('1')
# 
move('2')
move('3')
move('4')
