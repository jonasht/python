import pickle
import os

def str_ToList(lista):
    lista = lista.strip('[]')
    lista = lista.replace("'", '')
    lista = lista.replace("\\n", "\n")
    lista = lista.split(',')
    # print(type(lista), lista)
    return lista



def dumb(frames, path='framesB.txt'):
    with open(path, 'wb') as arq:
        pickle.dump(frames, arq)

def load(path='framesB.txt'):
    with open(path, 'rb') as arq:
        frames = pickle.load(arq)
        return frames
def load1(path='./assets/frames'):
    
    frames_file = os.listdir(path) 

    for frame_file in frames_file:
        path = path+'/'+frame_file
        print(path)
        # with open(path, 'rb') as arq:
        #     frames = pickle.load(arq)
        #     return frames

if __name__=='__main__':
    load1()
