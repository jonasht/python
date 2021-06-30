from posix import ST_NOATIME
from uteis import *
import colors as c



matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]
def colocarNumeros(matriz):
    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):

            if m == 'X':
                matriz[i][ii] = 3
            elif m == 'O':
                matriz[i][ii] = 2
            else:
                matriz[i][ii] = 0
    return matriz
                
def show(matriz):
    matriz = colocarNumeros(matriz)

    for ms in matriz:
        for m in ms:
            print(m, end='')
        print('',sum(ms))
        # print()
    # print()
    soma = 0
    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):
            soma += matriz[ii][i]
        print(soma, end='')
        soma = 0
    print()
mostrar(matriz)
colocar('O', 0, 0, matriz)
colocar('X', 0, 1, matriz)
colocar('O', 2, 2, matriz)
colocar('X', 1, 1, matriz)



mostrar(matriz)
show(matriz)


        

        
