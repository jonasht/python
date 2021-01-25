from time import sleep
from random import shuffle
lista = list(range(1, 11))

shuffle(lista)

mostrarLista = [([0 for i in range(10)]) for i in range(10)]
print()
def mostrar():
    for ls in mostrarLista:
        for l in ls:
            if l == True:
                print(f'{l} ', end='')
            else:
                print('  ', end='')
            #print(f'{l} ', end='')
        print()
    for i in lista:
        print(f'{i} ', end='')

#mostrarLista[1][1] = 1

for contador in range(len(lista)):
    for i, chars in enumerate(mostrarLista[::-1]):
        if lista[contador] == i: break        
        chars[contador] = 1
        sleep(.02)
        mostrar()



