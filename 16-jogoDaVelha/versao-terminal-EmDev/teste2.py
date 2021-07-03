from ia import *
import colors as c
from uteis import *

matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]


mostrar(matriz)
colocar('O', 0, 0, matriz)
colocar('X', 0, 1, matriz)
colocar('O', 2, 2, matriz)
colocar('X', 1, 1, matriz)
colocar('O', 2, 0, matriz)



mostrar(matriz)
mandarmatriz = matriz.copy()
jogada = fazerJogada(mandarmatriz)

colocar('X', jogada[0][0], jogada[0][1], matriz)
mostrar(matriz)


        

        
