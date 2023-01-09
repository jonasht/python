import os
import uteis
import colors as c
matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]

def limpar():
    os.system('clear')

def mostrar(matriz):
    limpar()
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
    

def verificadorDeVencer(quem):
    for i in range(3):
        if matriz[0][i] == quem:
            retornar = True

def colocar(char, x, y):
    x = int(x)
    y = int(y)
    if matriz[x][y] != 'X' or matriz[x][y] != 'O':
        matriz[x][y] = char
        return True
    else:
        return False
    
vez = ['X', 'O']

while True:
    mostrar(matriz)
    
    print(f'vez de {c.red}{vez[0]}{c.fim}' if vez[0] == 'X' else f'vez de {c.blue}{vez[0]}{c.fim}')
    lista = list(input('opcao:'))
    

    # s para sair
    if 's' in lista:
        print('saindo')
        break
    
    # colocando na posicao
    evento=colocar(vez[0], lista[0], lista[1])
    
    if uteis.verificar(vez[0], matriz):
        mostrar(matriz)
        print(f'{vez[0]} ganhou')
        break
    else:
        # ir para outra  vez
        if evento:
            vez.reverse()
        else:
            print('nao permitido colocar nesta posicao')
            

        
