def ehNumero(n):
    return n.isnumeric()
    
def ehLetra(char):
    return char.isalpha()

def separarNumero(caracteres):
    
    lista_chars = list(caracteres)
    
    numeros = list()
    numero = ''
    
    for chars in lista_chars:
        
        if chars.isnumeric() or chars == '-' or chars == '+':
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
        if letra.isalpha() and letra != '-' and letra != '+' :
            letras += letra
    
    return list(letras)


def temLetra_exceto(chars, exceto):
    # chars = strings com letras e numero, exceto = a letra que eh para ignorar
    # retorna true pq tem ou false porque nao
    
    chars = list(chars)
    sim = False
    
    for char in chars:
        if char.isalpha() and char != exceto:
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
    elif valor.isalpha():
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

