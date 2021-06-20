def ehNumero(n):
    try:
        int(n)
    except:
        return False
    else:
        return True
    
def ehString(char):
    if ehNumero(char):
        return False
    else:
        return True

def separarNum(caracteres):
    
    print('começo:',caracteres)
    lista_chars = list(caracteres)
    
    numeros = list()
    numero = ''
    
    for chars in lista_chars:
        
        if ehNumero(chars) or chars == '-' or chars == '+':
            numero += chars
        
        
        # if ehString(chars) and numero != '' and numero != '+' and numero != '-':
        elif numero != '':
            
            numeros.append(numero)
            numero = ''

    
    return numeros

# print(separarNum('52x78xxx'))