# arranjos ou vetores, ou arrays são os mesmos

def EncontrarElementosDuplicados(lista, m):
    # se a lista = vazia returna zero
    if not lista:
        return[]
    
    tabelaDeFrequncia = [0] * m
    duplicadas = []
    
    for i in range(len(lista)):
        for ii in range(i + 1, len(lista)):
            if lista[i] == lista[ii]:
                duplicadas.append(lista[ii])
                
    return duplicadas
print(f'elementos duplicados:')
elementos = EncontrarElementosDuplicados([1,2,1,1,1,1,2,2,3,4,8,8,9,5,7,5,6,90,99,99,99,10,54,55,55,41,63,45,69,74], 99)

for elemento in elementos:
    print(f'{elemento} ', end='')
print()