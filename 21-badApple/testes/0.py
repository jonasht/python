import pickle
from colorama import Back


lista = list(range(10))
algo = '@@@@@@\n@@@@@\n'
lista.append(algo)
algo = Back.GREEN +'          '+ Back.RESET 
lista.append(algo)

for l in lista:
    print(l)
def write(lista):
    with open('teste.txt', 'wb') as arq:
        pickle.dump(lista, arq)
        
def read():
    with open('teste.txt', 'rb') as arq:
        l = pickle.load(arq)
        return l

write(lista)
print(type(lista), lista)
for l in lista:
    print(l)