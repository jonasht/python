lista = '23456789'
lista = list(lista)
print(f'tamanho:{len(lista)}')

print(' '.join(lista))

# if len (lista) > 5:
print(lista)
lista.insert(6, '\n')
print(lista)
lista = ' '.join(lista)
print(lista)

print()
lista = list(lista)
print(lista)

while ' ' in lista:
    lista.remove(' ')
print(lista)
