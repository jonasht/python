
from random import shuffle
from os import system
import time
nomesObjetos = list(range(5))
shuffle(nomesObjetos)


def maneira():
    tamanho = len(nomesObjetos)
    for _ in range(tamanho):
        for i in range(tamanho):

            if i+1 != tamanho:
                if nomesObjetos[i] > nomesObjetos[i+1]:
                    guardarNumero = nomesObjetos[i]
                    nomesObjetos[i] = nomesObjetos[i+1]
                    nomesObjetos[i+1] = guardarNumero
            if i > 1:
                if nomesObjetos[tamanho-i+1] < nomesObjetos[tamanho-i]:
                    guardarNumero = nomesObjetos[tamanho-i]
                    nomesObjetos[tamanho-i] = nomesObjetos[tamanho-i+1]
                    nomesObjetos[tamanho-i+1] = guardarNumero
                
        # system('clear')
        print(*nomesObjetos)
        # time.sleep(.5)
            
maneira()