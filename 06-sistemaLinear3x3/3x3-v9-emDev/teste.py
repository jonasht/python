def ehNumero(n):
    try:
        int(n)
    except:
        return False
    else:
        return True
def TemNumero_list(lista):
    for valor in lista:
        if ehNumero(valor):
            return True
    return False

def filtrar(chave, valor):
    erro = False
    
    valorlista = list(valor)
 
    if chave in valorlista:
        qtdChave = valorlista.count(chave)
        print(valorlista)
        if TemNumero_list(valorlista) and qtdChave > 0:
                qtdChave -= 1
                print(valorlista)
                
        if valorlista[0] == '-' or valorlista[0] == '+':
            valor = valorlista[0] + str(qtdChave)
        else:
            valor = str(qtdChave)

    
    valor = int(valor)
    
    
    
    return chave, valor, erro
    

    
print(filtrar('x', '-xxxxxx'))
print(filtrar('y', '9y'))



