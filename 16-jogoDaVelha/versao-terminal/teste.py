from uteis import *
import colors as c



matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]

def pontuar(matriz, char):
    posicoesDeChar = []
    
    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):
            if m != char:
                matriz[i][ii] = 0
            mostrar(matriz)
            
    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):
            if m == char:
                posicoesDeChar.append([i, ii])
    for posicao in posicoesDeChar:
        matriz[posicao[0]+1][posicao[1]+1] += 1
        
    print(posicoesDeChar)
    mostrar(matriz)
mostrar(matriz)
colocar('O', 0, 0, matriz)
# colocar('O', 2, 2, matriz)

mostrar(matriz)

pontuar(matriz, 'O')

        

        
