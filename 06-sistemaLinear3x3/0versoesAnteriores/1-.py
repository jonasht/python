
# calculo linear 
# regra de cramer
# --------------------------------------------------
conta = [
    {'x': 1, 'y': 2, 'z': 1, '=': 8},
    {'x': 2, 'y':-1, 'z': 1, '=': 3},
    {'x': 3, 'y': 1, 'z':-1, '=': 2}
]
# --------------------------------------------------

def enfeitar():
    print('-' * 30)

def mostrar_conta(conta):
    for dic in conta:
        for chave, item in dic.items():
            if chave == '=':
                print(f' = {item}', end='')      
            else:
                if len(str(item)) == 1:
                    print(f'  {item}{chave}', end='') 
                else:
                    print(f' {item}{chave}', end='')
        print()


def montar_matriz(conta):
    matriz = [[], [], []]
    for i, dic in enumerate(conta):
        for chave, item in dic.items():
            if chave != '=':
                matriz[i].append(item)

    for i in range(3):
        for ii in range(2):
            matriz[i].append(matriz[i][ii])
    return matriz



def mostrar_matriz(matriz):
    
    for lista in matriz:
        for n in lista:
            if len(str(n)) == 1:
                print(f'  {n}', end='')
            else:
                print(f' {n}', end='')
        print()
def somarMatriz():
    multiplicacao = 1
    resultado = 0
    for seguinte in range(3):
        for i in range(3):
            multiplicacao *= lista_delta[i][i+seguinte]
        resultado += multiplicacao
        multiplicacao = 1
            
    for seguinte in range(3):
        for i in range(3):            
            multiplicacao *= -(lista_delta[-(i-2)][i+seguinte])
        resultado += multiplicacao
        multiplicacao = 1

        
    return resultado

print()
enfeitar()
print('conta:')
mostrar_conta(conta)
enfeitar()
print('lista delta:')


lista_delta = montar_matriz(conta)
mostrar_matriz(lista_delta)

enfeitar()
delta = somarMatriz()
print(f'delta = {delta}')
