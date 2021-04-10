from auro import *

# posicao atual de cada barra, onde ela está 
posicaoAtual = {}

# disponibilidade de cada parte na decida e subida, usando - +
disponivel = {
   'parte1': 7,
   'parte2': 7,
   'parte3': 7-4
}

# declarando as partes atuais
parte1 = []
parte2 = []
parte3 = ['1', '2', '3', '4']

# ----------------------------------
valorDeCadaBarra = {
   '1':1,
   '2':2,
   '3':3,
   '4':4}


def up(nome):
   
   # parte1 =-=-=-=-=-=-=-=-=-
   if posicaoAtual[nome] == 1:   
      for _ in range(0, disponivel['parte1']):
         backend.move(nome, '^')
         mostrar()
   
   # parte2 =-=-=-=-=-=-=-=-=-
   if posicaoAtual[nome] == 2:   
      for _ in range(0, disponivel['parte2']):
         backend.move(nome, '^')
         mostrar()

   # parte3 =-=-=-=-=-=-=-=-=-   
   if posicaoAtual[nome] == 3:   
      for _ in range(0, disponivel['parte3']):
         backend.move(nome, '^')
         mostrar()   
   
def mudarPartes(nomeParte, nome, para):
   if nomeParte == 1:
      parte1.remove(nome)
   elif nomeParte == 2:
      parte2.remove(nome)
   elif nomeParte == 3:
      parte3.remove(nome)
   
   if para == 1:
      parte1.append(nome)
   if para == 2:
      parte2.append(nome)
   if para == 3:
      parte3.append(nome)

def move(nome, opcao):
   parte = 0
   mudarPartes(posicaoAtual[nome], nome, opcao)
   
   if posicaoAtual[nome] == 3:
      if opcao == 1:
         parte = 30
         posicaoAtual[nome]=1
         disponivel['parte3'] += 1
         disponivel['parte1'] -= 1
         
      elif opcao == 2:
         parte = 15
         posicaoAtual[nome]=2
         disponivel['parte3'] += 1
         disponivel['parte2'] -= 1

      for _ in range(0, parte):
         backend.move(nome, '<')
         mostrar()
         
   elif posicaoAtual[nome] == 1:
      if opcao == 3:
         parte = 30
         posicaoAtual[nome]=3
         disponivel['parte1'] += 1
         disponivel['parte3'] -= 1

      elif opcao == 2:
         parte = 15
         posicaoAtual[nome]=2
         disponivel['parte1'] += 1
         disponivel['parte2']-= 1
      for _ in range(0, parte):
         backend.move(nome, '>')
         mostrar()
   elif  posicaoAtual[nome] == 2:
      if opcao == 1:
         parte = 15
         posicaoAtual[nome] = 1
         disponivel['parte2'] += 1
         disponivel['parte1'] -= 1
         
         for _ in range(0, parte):
            backend.move(nome, '<')
            mostrar()   
            
      elif opcao == 3:
         parte = 15
         posicaoAtual[nome] = 3
         disponivel['parte2'] += 1
         disponivel['parte3']-=1

         for _ in range(0, parte):
            backend.move(nome, '>')
            mostrar()
         

def down(nome):
   
   if posicaoAtual[nome] == 1:
      for _ in range(0, disponivel['parte1']):
         backend.move(nome, 'v')
         mostrar()   
         
   elif posicaoAtual[nome] == 2:
      for _ in range(0, disponivel['parte2']):
         backend.move(nome, 'v')
         mostrar()
   elif posicaoAtual[nome] == 3:
      for _ in range(0, disponivel['parte3']):
         backend.move(nome, 'v')
         mostrar()      

   # for _ in range(6-lenParte):
   #    backend.move(nome, 'v')
   #    mostrar()
      
fim = '\033[0m'
black = '\033[40m ' + fim 
red = '\033[41m '  + fim
green = '\033[42m ' + fim
yellow = '\033[43m ' + fim
blue = '\033[44m ' + fim 
pink = '\033[45m ' + fim 
white = '\033[107m ' + fim

def mostrar(tempo=.1):
   system('clear')
   # backend.mostrar()
   for chars in backend.desenho:
      for char in chars:
            if char == '1':
               print(f'{red}{red}', end='')
            elif char == '2':
               print(f'{green}{green}', end='')
            elif char == '3':
               print(f'{yellow}{yellow}', end='')
            elif char == '4':
               print(f'{blue}{blue}', end='')
            else:
               print(f'  ', end='')
      print()
   print('=-'*60 + '=')
   print('\t\t\t\t\t\ttorre de hanoi')
   sleep(tempo)
   # print('p:', parte1, parte2, parte3)
   # print(f'd:{disponivel}')
   # print(f'posicaoAtual: {posicaoAtual}')


backend = auroGame(56, 10, f' ')

print(backend.get_info())

def iniciar():
   parte3 = 45
   mostrar()

   backend.set_objeto(f'4', x=parte3+1, y=9, qtdCasas= 9 )
   mostrar(0)
   backend.set_objeto(f'3', x=parte3+2, y=8, qtdCasas=7)
   mostrar(0)
   backend.set_objeto(f'2', x=parte3+3, y=7, qtdCasas=5)
   mostrar(0)
   backend.set_objeto(f'1', x=parte3+4, y=6, qtdCasas=3)
   mostrar(0)
   
   # registrando a posicao atual de cada um na parte3
   posicaoAtual['1'] = 3
   posicaoAtual['2'] = 3
   posicaoAtual['3'] = 3
   posicaoAtual['4'] = 3
   
   
   
iniciar()



print(posicaoAtual)
# print('='*30)


up('1')
move('1', 2)
down('1')

up('2')
move('2', 1)
down('2')

up('1')
move('1', 1)
down('1')

up('3')
move('3', 2)
down('3')

up('1')
move('1', 3)
down('1')

up('2')
move('2', 2)
down('2')

up('1')
move('1', 2)
down('1')

up('4')
move('4',1)
down('4')

up('1')
move('1', 1)
down('1')

up('2')
move('2', 3)
down('2')

up('1')
move('1', 3)
down('1')

up('3')
move('3', 1)
down('3')

up('1')
move('1', 2)
down('1')

up('2')
move('2', 1)
down('2')

up('1')
move('1', 1)
down('1')
