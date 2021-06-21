def ehNumero(n):
    try:
        int(n)
    except:
        return False
    else:
        return True
    
def ehLetra(char):
    if ehNumero(char):
        return False
    else:
        return True

def separarNumero(caracteres):
    
    lista_chars = list(caracteres)
    
    numeros = list()
    numero = ''
    
    for chars in lista_chars:
        
        if ehNumero(chars) or chars == '-' or chars == '+':
            numero += chars
        
        elif numero != '':
            
            numeros.append(numero)
            numero = ''
    
    return numeros

# separar as letras 
def separarLetra(letras):
    lista_letras = list(letras)
    letras = ''

    for letra in lista_letras:
        if ehLetra(letra) and letra != '-' and letra != '+' :
            letras += letra
    
    return list(letras)


def temLetra_exceto(chars, exceto='x'):
    # chars = strings com letras e numero, exceto = a letra que eh para ignorar
    # retorna true pq tem ou false porque nao
    
    chars = list(chars)
    
    sim = False
    
    for char in chars:
        if ehLetra(char) and char != exceto:
            sim = True

            
    return sim
# print(separarNumero('52x78xxx'))