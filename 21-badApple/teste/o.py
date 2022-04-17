
lista = list()
for i in range(10):
    lista.append('@'*30)
    
    
print(type(lista), lista)

lista = str(lista)
print(type(lista), lista)

lista = ''.join(lista)
print(type(lista), lista)

print()
# lista = lista.replace('[', '')
# lista = lista.replace(']', '')
# lista = lista.replace("'"," "

lista = lista.strip('[]')
lista = lista.replace("'", '')
lista = lista.split(', ')
print(type(lista), lista)

for l in lista:
    print(l)
    

