from auro import *

# espacamento entre as barras
# esp = {
#    '1': 3,
#    '2': 2,5,
#    '3': 1,
#    '4': 0,}


def up(nome):
   ate = int(nome)+3
   
   for _ in range(1, ate):
      mostrar()
      backend.move(nome, '^')
   mostrar()

def move(nome, opcao, lado='<'):
   if opcao == 1:
      parte = 15 * 3
   if opcao == 2:
      parte = 15 * 2
   if opcao == 3:
      parte = 15 * 1
   
   for _ in range(1, parte):
      backend.move(nome, '<')
      mostrar(.01)
      
def down(nome, opcao):
#    for _ in range(disponivel['parte1']):
#       backend.move(nome, 'v')
#       mostrar()
   if opcao == 1:
      for _ in range(disponivel['parte1']):
            backend.move(nome, 'v')
            mostrar()      
      disponivel['parte1'] = disponivel['parte2'] - 1
   if opcao == 2:
      for _ in range(disponivel['parte2']):
         backend.move(nome, 'v')
         mostrar()
      disponivel['parte2'] = disponivel['parte2'] - 1

   mostrar()

def mostrar(tempo=.01):
   system('clear')
   backend.mostrar()
   sleep(tempo)


backend = auro(56, 10, f' ')
partes = 15

disponivel = {
   'parte1': 6,
   'parte2': 6
}

print(backend.get_info())

def iniciar():
   parte3 = partes * 3
   backend.mostrar()

   backend.set_objeto(f'4', x=parte3+1, y=9, qtdCasas= 9 )
   mostrar(0)
   backend.set_objeto(f'3', x=parte3+2, y=8, qtdCasas=7)
   mostrar(0)
   backend.set_objeto(f'2', x=parte3+3, y=7, qtdCasas=5)
   mostrar(0)
   backend.set_objeto(f'1', x=parte3+4, y=6, qtdCasas=3)
   mostrar(0)
iniciar()




print('='*30)
# print(backend.get_posicao()['1'])

up('1')
mostrar()

move('1', 1)
print(backend.get_info())

down('1', 1)

up('2')
move('2', 2)
down('2', 2)

up('3')
move('3', 1)
down('3', 1)

up('4')
move('4', 2)
down('4', 2)

# up('2')
# move('2', 2)
# down('2')

# up('3')