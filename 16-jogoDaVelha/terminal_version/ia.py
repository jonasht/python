# ainda em teste

from math import trunc
from uteis import *
from random import shuffle, choice

class Ia:
    def __init__(self, jogador):
        self.jogador = jogador.upper()
    
        # definindo rival 
        self.rival = 'O' if self.jogador == 'X' else 'X'
        
        print('rival:', self.rival)
        print('jogador:', self.jogador)
    # colocar numero no local de matriz
    def colocarNumeros(self, matriz):
        matrizNum = [[0 for _ in range(3)] for _ in range(3)]


        for i, ms in enumerate(matriz):
            for ii, m in enumerate(ms):

                if m == self.jogador:
                    matrizNum[i][ii] = 3
                elif m == self.rival:
                    matrizNum[i][ii] = 2
                else:
                    matrizNum[i][ii] = 0
        print('colocarNumero, matrizNum:', matrizNum)
        return matrizNum

    # somar numeros, de todas possibidades  
    def somarNumeros(self, matrizNum):
        matrizNum = self.colocarNumeros(matrizNum)
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
    def encontrarEspoco(self, opcao, matrizNum):
        fileira = []

        for i, ms in enumerate(matrizNum):
            print('i:', i, 'opcao:', opcao)
            # ||| 0, 1, 2
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
                if matrizNum[(i)][2-i] == 0:
                    fileira.append([i, 2-i])

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
        print('fileira:', fileira)
        shuffle(fileira)
        return choice(fileira)


    def fazerJogada(self, matriz):

        numeros, matrizNum = self.somarNumeros(matriz)
        maior = 0

        for char in numeros:
            if char > maior or char == 6:
                if char != 7 and char != 8:
                    maior = char

        print('maior:', maior)
        fileira = numeros.index(maior)

        print('retornarEspaço: fileira:', fileira, matrizNum)
        return self.encontrarEspoco(fileira, matrizNum)
    

# fazer a matriz
matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]

# iaX = Ia('x')

# colocar('o', 0, 0, matriz)
# mostrar(matriz)

# x, y = iaX.fazerJogada(matriz)
# colocar('x', x, y, matriz)
# mostrar(matriz)

# colocar('o', 1, 1, matriz)
# mostrar(matriz)

# x, y = iaX.fazerJogada(matriz)
# colocar('x', x, y, matriz)
# mostrar(matriz)

# colocar('o', 0, 2, matriz)
# mostrar(matriz)

# x, y = iaX.fazerJogada(matriz)
# colocar('x', x, y, matriz)
# mostrar(matriz)

import colors as c
# ia = []
# ia.append(Ia('x'))
# ia.append(Ia('o'))

iaX = Ia('x')
iaO = Ia('o')
while True:

    x, y = iaX.fazerJogada(matriz)
    colocar('x', x, y, matriz)
    mostrar(matriz)

    if verificar('x', matriz):
        print('x venceu')
        break
    

    x, y = iaO.fazerJogada(matriz)
    colocar('O', x, y, matriz)
    mostrar(matriz)

    if verificar('o', matriz):
        print('O venceu')
        break