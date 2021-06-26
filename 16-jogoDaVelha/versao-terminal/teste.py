

# faz a matriz de tres 
matriz = [['a', 'a', 'a'] for _ in range(3)]

# mostra no campo
def mostrar():
    for ms in matriz:
        for m in ms:
            print(f'{m} ', end='')
        print()

# simula colocando x ou o na matriz
def simular(onde='/', char='x'):
    if onde == '\\':
        for i in range(3):
            matriz[i][i] = char
    if onde == '/':
        for i in range(3):
            matriz[2-i][i] = char
    if onde == '0-':
        for i in range(3):
            matriz[0][i] = char
    if onde == '1-':
        for i in range(3):
            matriz[1][i] = char
            
    if onde == '2-':
        for i in range(3):
            matriz[2][i] = char
    if onde == '0|':
        for i in range(3):
            matriz[i][0] = char
    if onde == '1|':
        for i in range(3):
            matriz[i][1] = char       
    if onde == '2|':
        for i in range(3):
            matriz[i][2] = char


# verificar se o X ou O ganhou returnando verdadeiro
def verificar(char):
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


mostrar()
print()
print(verificar('x'))
simular('/')
mostrar()
print(verificar('x'))


