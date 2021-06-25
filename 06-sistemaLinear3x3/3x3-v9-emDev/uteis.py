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


def temLetra_exceto(chars, exceto):
    # chars = strings com letras e numero, exceto = a letra que eh para ignorar
    # retorna true pq tem ou false porque nao
    
    chars = list(chars)
    sim = False
    
    for char in chars:
        if ehLetra(char) and char != exceto:
            sim = True
    return sim


def filtrar(chave, valor):
    # filtrar chave e valor de um dicionaria{}
    
    erro = False
    frase = ''
    
    # conferindo se hah letra menos "chave"
    if temLetra_exceto(valor, chave):
        valor = 0
        erro = True
        frase = 'foi digitado um valor incorreto'

    # se tem letra 
    elif ehLetra(valor):
        # se tem numero no final de valor de dic{}

        if ehNumero(valor[-1]):
            
            frase = f'valor entendido: {valor}{chave}'
            valor += str(chave)
            
        erro = False    
        letras = separarLetra(valor)    
        numeros = separarNumero(valor)  
        valor = sum(map(int, numeros)) + (len(letras)-len(numeros)) 

    else:
        valor = int(valor)

    return chave, valor, erro, frase

# print(separarNumero('52x78xxx'))