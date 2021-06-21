from uteis import *



def temLetra_exceto(chars, exceto='x'):
    # chars = strings com letras e numero, exceto = a letra que eh para ignorar
    # retorna true pq tem ou false porque nao
    
    chars = list(chars)
    
    sim = False
    
    for char in chars:
        print('char:', char)
        if ehLetra(char) and char != exceto:
            sim = True

            
    return sim
        



print(temLetra_exceto('12xxax'))
print(temLetra_exceto('12xxxx'))