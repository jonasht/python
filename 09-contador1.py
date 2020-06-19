import random
import os

#feito no window/ it was made on windows
cont = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def l():
    print('\n', '=-=-'*15+'=')

def decimal():
    cont = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in cont:
        print(' \n', end='')
        for ii in cont:
            print(f'{i}{ii} ', end='')  

def duodecimal():
    cont = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'X', 'E']
    for i in cont:
        print(' \n', end='')
        for ii in cont:
            print(f'{i}{ii} ', end='')  

while 1:
    l()
    op = input('counting in/contar em\n1 decimal\n2 duodecimal\nop:')
    
    if int(op) == 0:
        break 
    elif int(op) == 1:
        
        decimal()
    elif int(op) == 2:
        l()
        duodecimal()