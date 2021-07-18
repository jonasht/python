from os import system
import time

azul = '\033[44m'
f = '\033[0m'
def mostrar(nss):
    for ns in nss:
        for n in ns:
            print(f' {n}', end='')
        print()
    print()
def inverterMatriz(nss, posicao = 0):

    if posicao == 0:
        for ns in nss:
            for n in ns:
                if n == 1:
                    print(f'{azul}  {f}', end='')
                else:
                    print(f'  ', end='')
            print()
            

    if posicao == 1:
        for i in range(len(nss)):
            for ii in reversed(range(len(nss))):
                if nss[ii][i] == 1:
                    print(f'{azul}  {f}', end='')
                else:
                    print(f'  ', end='')
            print()    
            
    if posicao == 2:
        for ns in reversed(nss):
            for n in reversed(ns):
                if n == 1:
                    print(f'{azul}  {f}', end='')
                else:
                    print(f'  ', end='')
            print()
            
    
    if posicao == 3:        
        for i in reversed(range(len(nss))):
            for ii in range(len(nss)):
                if nss[ii][i] == 1:
                    print(f'{azul}  {f}', end='')
                else:
                    print(f'  ', end='')

            print()    
    
matriz = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

]
matriz1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

]


def limpar():
    time.sleep(.05)    
    system('clear')

print()
#mostrar(matriz)

for i in range(1000):
    inverterMatriz(matriz, 0)
    limpar()
    inverterMatriz(matriz1, 0)
    limpar()    
    inverterMatriz(matriz, 1)
    limpar()
    inverterMatriz(matriz1, 1)
    limpar()    
    inverterMatriz(matriz, 2)
    limpar()
    inverterMatriz(matriz1, 2)
    limpar()    
    inverterMatriz(matriz, 3)
    limpar()
    inverterMatriz(matriz1, 3)
    limpar()
inverterMatriz(matriz1, 0)

inverterMatriz(matriz1, 1)

inverterMatriz(matriz1, 2)

inverterMatriz(matriz1, 3)