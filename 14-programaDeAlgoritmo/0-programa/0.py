from time import sleep
from random import shuffle
lista = list(range(1, 11))

shuffle(lista)


print()


def Mostrar(mostrarLista):
    print()
    for cs in mostrarLista:
        for c in cs:
            if c == 1:
                print(f'{c} ', end='')
            else:
                print('  ', end='')
            
        print()
    
#mostrarLista[1][1] = 1
def converterPMostrar():
    
    mostrarLista = [([0 for i in range(10)]) for i in range(10)]
    for contador in range(len(lista)):
        for i, chars in enumerate(mostrarLista[::-1]):
            if lista[contador] == i: break        
            chars[contador] = 1
            Mostrar(mostrarLista)
    


print(lista)


def Maneira():
    guardarNumero = 0
    
    for c in range(len(lista)):
        for i in range(len(lista)):
            sleep(1)

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