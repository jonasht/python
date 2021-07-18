
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


def montar_matriz(conta, op='='):
    matriz = [[], [], []]
    
    if op == '=':
        for i, dic in enumerate(conta):
            for chave, item in dic.items():
                if chave != '=':
                    matriz[i].append(item)
                    
    else:
        for i, dic in enumerate(conta):
            for chave, item in dic.items():
                if chave != '=':                
                    if chave == op:
                        matriz[i].append(conta[i]['='])
                    else:
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


def somarMatriz(matriz):
    
    multiplicacao = 1
    resultado = 0
    for seguinte in range(3):
        for i in range(3):
            multiplicacao *= matriz[i][i+seguinte]
        resultado += multiplicacao
        multiplicacao = 1
            
    for seguinte in range(3):
        for i in range(3):            
            multiplicacao *= -(matriz[-(i-2)][i+seguinte])
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


delta = somarMatriz(lista_delta)
print(f'delta = {delta}')
enfeitar()

lista_deltaX = montar_matriz(conta,'x')
mostrar_matriz(lista_deltaX)
deltaX = somarMatriz(lista_deltaX)
print(f'deltaX = {deltaX}')

enfeitar()

matriz_deltaY = montar_matriz(conta,'y')
mostrar_matriz(matriz_deltaY)

deltaY = somarMatriz(matriz_deltaY)
print(f'deltaX = {deltaY}')

enfeitar()
matriz_deltaZ = montar_matriz(conta, 'z')
mostrar_matriz(matriz_deltaZ)

deltaZ = somarMatriz(matriz_deltaZ)
print(f'deltaZ = {deltaZ}')

enfeitar()
