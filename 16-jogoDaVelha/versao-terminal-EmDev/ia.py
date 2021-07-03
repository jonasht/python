import colors as c
from uteis import *

# matrizNum = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]

def find(lista, oque):
    oque = str(oque)
    lista = map(str, lista)
    
    for i, char in enumerate(lista):
        if char == oque:
            return i
            
def colocarNumeros(cmatrizNum):
    
    for i, ms in enumerate(cmatrizNum):
        for ii, m in enumerate(ms):

            if m == 'X':
                cmatrizNum[i][ii] = 3
            elif m == 'O':
                cmatrizNum[i][ii] = 2
            else:
                cmatrizNum[i][ii] = 0
    return cmatrizNum
                
def somarNumeros(matrizNum):
    matrizNum = colocarNumeros(matrizNum)
    numeros = []
    soma = 0

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
    # print(numeros)
    return numeros

# encontrar espaca na matrizNum para poder colocar em uma determinada fileira
def encontrarEspoco(opcao, matrizNum):
    fileira = []

    for i, ms in enumerate(matrizNum):
        if opcao == 1:
            if matrizNum[i][1]== 0:
                fileira.append([i, 1])
    # print(fileira)
    return fileira


def fazerJogada(matrizNum):
    numeros = somarNumeros(matrizNum)

    maior = 0
    for char in numeros:
        # print(char)
        # maior 
        if char > maior and char <= 6:
            maior = char
    
    # print(maior)
    
    fileira = find(numeros, maior)
    
    return encontrarEspoco(fileira, matrizNum)
    