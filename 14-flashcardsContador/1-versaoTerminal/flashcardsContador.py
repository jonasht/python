# versao 3
# versao 3: deixado mais bonito visualmente

from Soma import *


# cores para definir
fim = '\033[0m'
black = '\033[40m'  
red = '\033[31m'  
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'  
pink = '\033[35m' 
white = '\033[107m'

# definindo soma
recomeçar = Soma()
começar = Soma()

def mostrar():
    system('clear')
    print('digite 0 para sair')
    
    
    print('=-'*30+'=')
    print(f'|\tCartas para ReComeçar: {green}{recomeçar.Somar()}{fim}')
    print(f'|\tCartas para   Começar: {blue}{começar.Somar()}{fim}')    
    print(f'|\tFaltam {red}{30-(recomeçar.Somar()+começar.Somar())}{fim}       Total: {blue}{recomeçar.Somar()+começar.Somar()}{fim}')

while True:
    mostrar()
    n = input(f'|\tNumero Para ReComeçar: ')
    if n == '0': break
    recomeçar.set_numeroDeCartas(n)
    
while True:
    mostrar()    
    n = input(f'|\tNumero Para   Começar: ')
    if n == '0': 
        break    
    começar.set_numeroDeCartas(n)

mostrar()
print('=-'*30+'=')
print('\n')