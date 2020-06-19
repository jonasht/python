import random
import os

#feito no window/ it was made on windows
cont = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def l():
    print('=-=-'*15,'=')

for i in cont:
    print(' \n', end='')
    for ii in cont:
        print(f'{i}{ii}', end=' ')  
