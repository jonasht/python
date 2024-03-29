# from ia import *
import colors as c
from uteis import *
from random import shuffle

            
# colocar numero no local de matriz
def colocarNumeros(matriz):
    matrizNum = [[0 for _ in range(3)] for _ in range(3)]

    for i, ms in enumerate(matriz):
        for ii, m in enumerate(ms):

            if m == 'X':
                matrizNum[i][ii] = 3
            elif m == 'O':
                matrizNum[i][ii] = 2
            else:
                matrizNum[i][ii] = 0
    print('colocarNumero, matrizNum:', matrizNum)
    return matrizNum

# somar numeros, de todas possibidades  
def somarNumeros(matrizNum):
    matrizNum = colocarNumeros(matrizNum)
    numeros = []
    soma = 0
    
    for i, ms in enumerate(matrizNum):
        for ii, m in enumerate(ms):
            soma += matrizNum[ii][i]
        numeros.append(soma)
        soma = 0
    
    soma = 0
    # /
    for i in range(3):
            soma += matrizNum[2-i][i]

    # soma todas as fileiras
    numeros.append(soma)
    for ms in matrizNum:
        numeros.append(sum(ms))

    soma=0
    # \
    for i in range(3):
        soma += matrizNum[i][i]
    
    numeros.append(soma)
    
    print('somar numeros: numeros:', numeros)
    return numeros, matrizNum

# encontrar espaca na matrizNum para poder colocar em uma determinada fileira
def encontrarEspoco(opcao, matrizNum):
    fileira = []

    for i, ms in enumerate(matrizNum):
        # ||| 1,2,3
        if opcao == 0:
            if matrizNum[i][0] == 0:
                fileira.append([i, 0])
        elif opcao == 1:
            if matrizNum[i][1] == 0:
                fileira.append([i, 1])        
        elif opcao == 2:
            if matrizNum[i][2] == 0:
                fileira.append([i, 2])
        # / 3
        elif opcao == 3:
            if matriz[2-i][i] == 0:
                fileira.append([2-i, i])

        # --- 4
        elif opcao == 4:
            if matrizNum[0][i] == 0:
                fileira.append([0, i])
        elif opcao == 5:
            if matrizNum[1][i] == 0:
                fileira.append([1, i])
        elif opcao == 6:
            if matrizNum[2][i] == 0:
                fileira.append([2, i])    
        # =======================================
        # \ 7
        elif opcao == 7:
            if matrizNum[i][i] == 0:
                fileira.append([i, i])
    shuffle(fileira)
    print('fileira:', fileira)
    return fileira[0]


def fazerJogada(matriz):

    numeros, matrizNum = somarNumeros(matriz)
    maior = 0
    
    for char in numeros:
        if (char > maior and char <= 6) and char != 5:
            maior = char
        
    print('maior:', maior)
    fileira = numeros.index(maior)
    
    print('retornarEspaço: fileira:', fileira, matrizNum)
    return encontrarEspoco(fileira, matrizNum)
    

# fazer a matriz
matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]


# mostrar(matriz)

# colocar('O', 0, 0, matriz)
# mostrar(matriz)


# colocar('x', 0, 1, matriz)
# mostrar(matriz)

# colocar('o', 1, 0, matriz)
# # colocar('x', 1, 1, matriz)
# x, y = fazerJogada(matriz)
# print('x:', x, 'y:', y)

# mostrar(matriz)

colocar('o', 0, 0, matriz)
mostrar(matriz)

x, y = fazerJogada(matriz)
colocar('x', x, y, matriz)
mostrar(matriz)

colocar('o', 1, 1, matriz)
mostrar(matriz)

x, y = fazerJogada(matriz)
colocar('x', x, y, matriz)
mostrar(matriz)

colocar('o', 0, 2, matriz)
mostrar(matriz)

x, y = fazerJogada(matriz)
colocar('x', x, y, matriz)
mostrar(matriz)
