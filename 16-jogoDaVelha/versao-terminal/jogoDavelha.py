import uteis
import colorama
matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]



def mostrar(matriz):
    print('-'*22)
    for linhas in matriz:
        for char in linhas:
            if char == 'O' or char == 'X':
                print(f'|   {char}  ', end='')
            else:
                print(f'|   {char} ', end='')
        print('|')
        print('-'*22)
        

        
def colocar(char, x, y):
    x = int(x)
    y = int(y)
    if matriz[x][y] == 'X' or matriz[x][y] == 'O' :
        return False
    else:
        matriz[x][y] = char
        return True
    
vez = ['X', 'O']

while True:
    
    
    verificacaoX = uteis.verificar('X', matriz)
    verificacaoO = uteis.verificar('O', matriz)
    

    if verificacaoX:
        print(f'X ganhou')
        break
    elif verificacaoO:
        print(f'O ganhou')
        break
    
    mostrar(matriz)
    print(f'vez de {vez[0]}')
    lista = list(input('opcao:'))
    

    # s para sair
    if 's' in lista:
        print('saindo')
        break
    
    # colocando na posicao (na matriz)
    evento=colocar(vez[0], lista[0], lista[1])
    
    # ir para outra  vez
    if evento:
        vez.reverse()
    else:
        print('nao permitido colocar nesta posicao')
        

    
mostrar(matriz)