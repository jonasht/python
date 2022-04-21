import pickle
from colorama import Back

def str_ToList(lista):
    lista = lista.strip('[]')
    lista = lista.replace("'", '')
    lista = lista.replace("\\n", "\n")
    lista = lista.split(',')
    # print(type(lista), lista)
    return lista

def read(path='./assets/framesb.txt') -> list:    
    frame = ''
    with open(path, 'r') as arq:
        frames = arq.read()
        # print(frames)
        return frames

def save(string, nameArq):
    string = str(string)
    with open(nameArq, 'w') as arq:
        arq.write(string)

def dumb(frames, path='framesB.txt'):
    with open(path, 'wb') as arq:
        pickle.dump(frames, arq)

def load(path='framesB.txt'):
    with open(path, 'rb') as arq:
        frames = pickle.load(arq)
        return frames

if __name__=='__main__':
    pass
