lista = [1, 2, 3, 4, 5, 6, '\n', 7, 8, 9]
print(lista)


lista = list(map(str, lista))
print(lista)

print()
lista = list(' '.join(lista))

print(lista.pop(6))

print(lista)
