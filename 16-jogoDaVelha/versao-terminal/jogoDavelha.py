import sys
matriz = [['1', '1', '1'] for _ in range(3)]



def mostrar(matriz):
    print('-'*20)
    for linhas in matriz:
        for char in linhas:
            if char == '1':
                print(f'|     ', end='')
            else:

                print(f'|  {char}  ', end='')
        print('|')

        
def colocar(char, x, y):
    x = int(x)
    y = int(y)
    if matriz[x][y] == '1':
        matriz[x][y] = char
        return True
    else:
        return False
    
vez = ['X', 'O']

while True:
    mostrar(matriz)
    
    print(f'vez de {vez[0]}')
    lista = list(input('opcao:'))
    

    # s para sair
    if 's' in lista:
        print('saindo')
        break
    
    # colocando na posicao
    evento=colocar(vez[0], lista[0], lista[1])
    
    # ir para outra  vez
    if evento:
        vez.reverse()
    else:
        print('nao permitido colocar nesta posicao')
        

    
mostrar(matriz)