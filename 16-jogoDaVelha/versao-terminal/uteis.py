import os
import colors as c

# verificar se o X ou O ganhou returnando verdadeiro, matriz = eh jogo da velha
def verificar(char, matriz):
    # char = caracter para X ou O ou outro que quiser pode verificar se ganhou
    # 0 --- posicao
    if matriz[0][0] == char and matriz[0][1] == char and matriz[0][2] == char:
        return True
    
    # 1 --- posicao
    elif matriz[1][0] == char and matriz[1][1] == char and matriz[1][2] == char:
        return True

    # 2 --- posicao
    elif matriz[2][0] == char and matriz[2][1] == char and matriz[2][2] == char:
        return True
    
    # 0 |   posicao
    elif matriz[0][0] == char and matriz[1][0] == char and matriz[2][0] == char:
        return True 
    # 1 |
    elif matriz[0][1] == char and matriz[1][1] == char and matriz[2][1] == char:
        return True   
    # 2 |   posicao
    elif matriz[0][2] == char and matriz[1][2] == char and matriz[2][2] == char:
        return True         
    # \     posicao
    elif matriz[0][0] == char and matriz[1][1] == char and matriz[2][2] == char:
        return True 
    # /     posicao
    elif matriz[2][0] == char and matriz[1][1] == char and matriz[0][2] == char:
        return True 
    else:
        return False
    
def limpar():
    os.system('clear')

def mostrar(matriz):
    # limpar()
    print('-'*22)
    for linhas in matriz:
        for char in linhas:
            if char == 'X':
                print(f'|{c.red}  {char}  {c.fim}', end='')
            elif char == 'O':
                print(f'|{c.blue}  {char}  {c.fim}', end='')
            else:
                print(f'|  {char}  ', end='')
        print('|')
    print('-'*22)
    


def colocar(char, x, y, matriz):
    x = int(x)
    y = int(y)
    if matriz[x][y] != 'X' or matriz[x][y] != 'O':
        matriz[x][y] = char
        return True
    else:
        return False
    