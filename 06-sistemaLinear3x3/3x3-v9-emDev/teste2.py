from uteis import *



# numero = separarNum('-598xxx21x')
# print(numero)

def separarLetra(letras):
    lista_letras = list(letras)
    letras = ''

    
    for letra in lista_letras:
        if ehString(letra) and letra != '-' and letra != '+' :
            letras += letra
    
    return list(letras)
            
letras = separarLetra('-598xxx21x')
print(letras)


