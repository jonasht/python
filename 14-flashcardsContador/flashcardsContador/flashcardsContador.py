from Soma import *
from os import system
  
recomeçar = Soma()
começar = Soma()
def mostrar():
    system('clear')
    print('digite 0 para sair')
    
    print('=-'*40+'=')
    print(f'|\tCartas para ReComeçar: {recomeçar.Somar()}')
    print(f'|\tCartas para   Começar: {começar.Somar()}')    
    print(f'|\t                Total: {recomeçar.Somar()+começar.Somar()}')


while 1:
    mostrar()
    n = input(f'|\tnumero Para ReComeçar:')
    if n == '0': break
    recomeçar.set_numeroDeCartas(n)
    
while 1:
    mostrar()    
    n = input(f'|\tnumero Para   Começar: ')
    if n == '0': break    
    começar.set_numeroDeCartas(n)

mostrar()