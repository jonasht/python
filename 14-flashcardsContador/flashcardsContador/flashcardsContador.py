from Soma import *
from os import system
  
recomeçar = Soma()
começar = Soma()
def mostrar():
    system('clear')
    print('=-'*40+'=')
    print(f'cartas para recomeçar: {recomeçar.Somar()}')
    print(f'cartas para recomeçar: {começar.Somar()}')    
    print(f'                total: {recomeçar.Somar()+começar.Somar()}')


while 1:
    mostrar()
    n = input(f'n Para ReComeçar:')
    if n == '0': break
    recomeçar.set_numeroDeCartas(n)
    
while 1:
    mostrar()    
    n = input(f'n Para Começar: ')
    if n == '0': break    
    começar.set_numeroDeCartas(n)

mostrar()