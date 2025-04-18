from auro import *

# posicao atual de cada barra, onde ela está 
posicaoAtual = {}

# disponibilidade de cada parte na decida e subida, usando - +
disponivel = {
   'parte1': 7,
   'parte2': 7,
   'parte3': 7-4
}

# declarando as partes atuais, onde cada barra estah
parte1 = []
parte2 = []
parte3 = ['1', '2', '3', '4']

# valor de cada barra para poder saber seu peso
# ----------------------------------
valorDeCadaBarra = {
   '1':1,
   '2':2,
   '3':3,
   '4':4}

# descer barra | nome = nome da barra
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

# mover a barra | nome = nome da barra, opcao = para onde barra vai (parte1, parte2, parte3)
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
         
# descer para baixo | nome = nome da barra
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


# cores para poder pintar os graficos
fim = '\033[0m'
black = '\033[40m ' + fim 
red = '\033[41m '  + fim
green = '\033[42m ' + fim
yellow = '\033[43m ' + fim
blue = '\033[44m ' + fim 
pink = '\033[45m ' + fim 
white = '\033[107m ' + fim

# mostrar, serve para mostrar na tela os graficos TUI
def mostrar(tempo=.1):
   frame = ''
   system('clear')
   
   # fazendo a frame
   for chars in backend.desenho:
      for char in chars:
            match char:
               case '1':
                  frame += f'{red}{red}'
               case '2':
                  frame += f'{green}{green}'
               case '3':
                  frame += f'{yellow}{yellow}'
               case '4':
                  frame += f'{blue}{blue}'
               case _:
                  frame += f'  '
      frame += '\n'
      
   print(frame[:-1])
   print(' '*15+'=-'*50 + '=')
   print('\t\t\t\t\t\t\tTorre de Hanoi')
   sleep(tempo)

# chamando o auro game
backend = auroGame(56, 10, f' ')

print(backend.get_info())

# funcao para iniciar, declarando onde cada barra estarah
def iniciar():
   tamanhoDasPartes = 45
   mostrar()

   backend.set_objeto(f'4', x=tamanhoDasPartes+1, y=9, qtdCasas= 9 )
   mostrar(0)
   backend.set_objeto(f'3', x=tamanhoDasPartes+2, y=8, qtdCasas=7)
   mostrar(0)
   backend.set_objeto(f'2', x=tamanhoDasPartes+3, y=7, qtdCasas=5)
   mostrar(0)
   backend.set_objeto(f'1', x=tamanhoDasPartes+4, y=6, qtdCasas=3)
   mostrar(0)
   
   # registrando a posicao atual de cada um na parte3
   posicaoAtual['1'] = 3
   posicaoAtual['2'] = 3
   posicaoAtual['3'] = 3
   posicaoAtual['4'] = 3
   
   
# iniciando a fucao para começar 
iniciar()
def mover(nome, onde):
   up(nome)
   move(nome, onde)
   down(nome)

# fazendo a movimentacao por movimentacao de barra (barra de cores)
mover('1', 2)
mover('2', 1)
mover('1', 1)
mover('3', 2)
mover('1', 3)
mover('2', 2)
mover('1', 2)
mover('4', 1)
mover('1', 1)
mover('2', 3)
mover('1', 3)
mover('3', 1)
mover('1', 2)
mover('2', 1)
mover('1', 1)

# fim de programa
# auro game é codigo feito por mim 