
def str_ToList(lista):
    lista = lista.strip('[]')
    lista = lista.replace("'", '')
    lista = lista.replace("\\n", "\n")
    lista = lista.split(',')
    # print(type(lista), lista)
    return lista

def read(path='./assets/frames0.txt') -> list:    
    frame = ''
    with open(path, 'r') as arq:
        frames = arq.read()
        # print(frames)
        return frames

def save(string, nameArq):
    string = str(string)
    with open(nameArq, 'w') as arq:
        arq.write(string)
        

