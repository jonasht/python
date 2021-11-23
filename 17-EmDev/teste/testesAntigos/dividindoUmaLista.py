lista = list(range(25))

print(lista)




c = 0

lista_Dividida = []
print(lista[5:-15])
print(lista[0:-20])

print()

tmn = len(lista)

for i in range(0, tmn, 5):
    print(i, tmn-i-5)


print()

for i in range(0, 20, 5):
    print(i, tmn-i-5)
    lista_Dividida.append(lista[i:-(tmn-i-5)])

    print('i:', i, 'l:', lista_Dividida)

print(lista)
print(lista_Dividida)

