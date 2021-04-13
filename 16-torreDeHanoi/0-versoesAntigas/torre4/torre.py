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
   


def move(nome, opPartes):
   if opPartes == 1:
      parte = partes * 1
   if opPartes == 2:
      parte = partes * 2
   if opPartes == 3:
      parte = partes * 3
      
   
   info = backend.get_posicao()[nome]
   
   for i in range(1, parte):
      backend.desenhar(info['nome'], info['x']-i, info['y'], info['qtdCasas'])
      backend.apagar(backend.get_posicao()[nome]['x'] + info['qtdCasas'], info['y'], 1)
      
      sleep(.01)
      system('clear')
      backend.mostrar()
      # print(info['nome'], 'x:', info['x']-i, 'y:', info['y'], 'qrdCasas:', 'qtdCasas:', info['qtdCasas'])
      # print('apagar: ', 'x:', info['x']+3, 'y:', info['y'], 'qrdCasas:', info['qtdCasas'])

registrar = {}
registrar['desenhar'] = []
registrar['  apagar'] = []

def down(nome):
   
   for i in reversed(range(1, 3)):
      
      info = backend.get_posicao()[nome]
      backend.desenhar(info['nome'], info['x'], info['y']+i, info['qtdCasas'])
      # backend.apagar(info['x'], info['y']+i-1, info['qtdCasas'])
      sleep(.5)
      system('clear')
      backend.mostrar()
      
      registrar['desenhar'].append([info['x'], info['y']+i, info['qtdCasas']])
      # registrar['  apagar'].append([info['x'], info['y']+i-1, info['qtdCasas']])
   
backend = auro(56, 10, f' ')

partes = 15



def iniciar():
   parte3 = partes * 3
   backend.mostrar()
   print('----------------------------------------')
   backend.desenhar(f'4', x=parte3+1, y=9, qtdCasas= 9 )
   magica()
   backend.mostrar()
   backend.desenhar(f'3', x=parte3+2, y=8, qtdCasas=7)
   magica()
   backend.mostrar()
   backend.desenhar(f'2', x=parte3+3, y=7, qtdCasas=5)
   magica()
   backend.mostrar()
   backend.desenhar(f'1', x=parte3+3, y=6, qtdCasas=3)
   magica()
   backend.mostrar()
iniciar()



print('='*30)
# print(backend.get_posicao()['1'])

up('1')
move('1', 3)
down('1')

up('2')
move('2', 2)
down('2')

up('3')
# down('1')
# move('2')
# move('3')
# move('4')

for k, i in  registrar.items():
   print(k, ':', i)