

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

# verificar X ou O ganhou, retornar true = ganhou, false = nao ganhou
def verificarXO(matriz):
    return verificar('X', matriz), verificar('O', matriz)


def mostrar(matriz):
    print('-'*22)
    for linhas in matriz:
        for char in linhas:
            if char == 'O' or char == 'X':
                print(f'|   {char}  ', end='')
            else:
                print(f'|  {char}  ', end='')
        print('|')
        print('-'*22)
        

# char = X ou O, x e y = posicao, matriz = é a matriz

def colocar(char, x, y, matriz):
    char = char.upper()
    x = int(x)
    y = int(y)
    

    matriz[x][y] = char
    return matriz
    
# vez = ['X', 'O']
# 
# while True:
    # 
    # 
    # verificacaoX = uteis.verificar('X', matriz)
    # verificacaoO = uteis.verificar('O', matriz)
    # 
# 
    # if verificacaoX:
        # print(f'X ganhou')
        # break
    # elif verificacaoO:
        # print(f'O ganhou')
        # break
    # 
    # mostrar(matriz)
    # print(f'vez de {vez[0]}')
    # lista = list(input('opcao:'))
    # 
# 
    # s para sair
    # if 's' in lista:
        # print('saindo')
        # break
    # 
    # colocando na posicao (na matriz)
    # evento=colocar(vez[0], lista[0], lista[1])
    # 
    # ir para outra  vez
    # if evento:
        # vez.reverse()
    # else:
        # print('nao permitido colocar nesta posicao')
        # 
# 
    # 
# mostrar(matriz)