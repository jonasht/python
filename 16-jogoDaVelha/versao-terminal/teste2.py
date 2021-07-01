from ia import *
import colors as c
from uteis import *

matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]

# def find(lista, oque):
#     oque = str(oque)
#     lista = map(str, lista)
    
#     for i, char in enumerate(lista):
#         if char == oque:
#             return i
            
# def colocarNumeros(cmatriz):
    
#     for i, ms in enumerate(cmatriz):
#         for ii, m in enumerate(ms):

#             if m == 'X':
#                 cmatriz[i][ii] = 3
#             elif m == 'O':
#                 cmatriz[i][ii] = 2
#             else:
#                 cmatriz[i][ii] = 0
#     return cmatriz
                
# def somarNumeros(matriz):
#     matriz = colocarNumeros(matriz)
#     numeros = []
#     soma = 0

#     soma = 0
#     for i, ms in enumerate(matriz):
#         for ii, m in enumerate(ms):
#             soma += matriz[ii][i]
#         numeros.append(soma)
            
#         soma = 0
    
#     soma = 0
    
#     # /
#     for i in range(3):
#             soma += matriz[2-i][i]

#     # soma todas as fileiras
#     numeros.append(soma)
#     for ms in matriz:
#         numeros.append(sum(ms))

#     soma=0
#     # \
#     for i in range(3):
#         soma += matriz[i][i]
    
#     numeros.append(soma)
#     # print(numeros)
#     return numeros

# # encontrar espaca na matriz para poder colocar em uma determinada fileira
# def encontrarEspoco(opcao, matriz):
#     fileira = []

#     for i, ms in enumerate(matriz):
#         if opcao == 1:
#             if matriz[i][1]== 0:
#                 fileira.append([i, 1])
#     # print(fileira)
#     return fileira


# def fazerJogada(matriz):
#     numeros = somarNumeros(matriz)
#     print(numeros)
#     maior = 0
#     for char in numeros:
#         print(char)
#         # maior 
#         if char > maior and char <= 6:
#             maior = char
    
    # print(maior)
    # 
    # fileira = find(numeros, maior)
    # 
    # return encontrarEspoco(fileira, matriz)
    
mostrar(matriz)
colocar('O', 0, 0, matriz)
colocar('X', 0, 1, matriz)
colocar('O', 2, 2, matriz)
colocar('X', 1, 1, matriz)
colocar('O', 2, 0, matriz)



mostrar(matriz)
# mandarmatriz = matriz[:]
jogada = fazerJogada(matriz)

colocar('X', jogada[0][0], jogada[0][1], matriz)
mostrar(matriz)


        

        
