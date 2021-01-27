from time import sleep
from random import shuffle
from os import system

f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red

# definição do tamanho da lista
tamanhoDaLista = 30
lista = list(range(1, tamanhoDaLista))

shuffle(lista)


print()

# mostrar lista, serve para mostrar a lista de forma legal
def Mostrar(mostrarLista):
    system('clear')
    print()
    for cs in mostrarLista:
        for c in cs:
            if c == 1:
                print(f'{bgBlue} {c} {f}', end='')
            else:
                print('   ', end='')
        print()                
    #mostrarLista.clear()

    
    
#mostrarLista[1][1] = 1

# aqui serve para tranformar uma lista em matrix para mostrar() conseguir mostrar
def converterPMostrar():
    
    mostrarLista = [([0 for i in range(tamanhoDaLista)]) for i in range(tamanhoDaLista)]
    for contador in range(len(lista)):
        for i, chars in enumerate(mostrarLista[::-1]):
            if lista[contador] == i: break        
            chars[contador] = 1
    Mostrar(mostrarLista)
    mostrarLista.clear()
    sleep(.02)    


print(lista)


def Maneira():
    guardarNumero = 0
    
    for c in range(len(lista)):
        for i in range(len(lista)):


            #print(i, len(lista))
            if i+1 == len(lista):
                continue
            else:
                if lista[i] > lista[i+1]:
                    guardarNumero = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = guardarNumero
                converterPMostrar()
Maneira()