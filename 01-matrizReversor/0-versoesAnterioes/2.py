def mostrar(nss):
    for ns in nss:
        for n in ns:
            print(f' {n}', end='')
        print()
    print()
def inverterMatriz(nss, posicao = 0):

    if posicao == 0:
        for ns in nss:
            for n in ns:
                print(f' {n}', end='')
            print()
            

    if posicao == 1:
        for i in range(len(nss)):
            for ii in reversed(range(len(nss))):
                print(f' {nss[ii][i]}', end='')
            print()    
            
    if posicao == 2:
        for ns in reversed(nss):
            for n in ns:
                print(f' {n}', end='')
            print()
            
    
    if posicao == 3:        
        for i in range(len(nss)):
            for ii in range(len(nss)):
                print(f' {nss[ii][i]}', end='')
            print()    
    
matriz = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

]



print()
#mostrar(matriz)
inverterMatriz(matriz, 0)
print()
inverterMatriz(matriz, 1)
print()
inverterMatriz(matriz, 2)
print()
inverterMatriz(matriz, 3)
print()

