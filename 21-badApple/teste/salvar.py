
def save(string):
    string = str(string)
    with open('salvar.txt', 'w') as arq:
        arq.write(string)
        

if __name__ == '__main__':
    algo = list('asfasfasdfasfsf')
    print(algo)
    lista = list()
    for i in range(1000):
        lista.append(algo)
    
    matriz = list()
    
    for i in range(1000):
        matriz.append(lista)
    
