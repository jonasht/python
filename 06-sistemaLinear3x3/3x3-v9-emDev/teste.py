from uteis import *


def filtrar(chave, valor):
    erro = False
    

    if temLetra_exceto(valor, chave):
        valor = 0
        erro = True
        print('foi digitado um valor incorreto')
    elif ehLetra(valor):
        if ehNumero(valor[-1]):
            valor = 0
            erro = True
            print('nao consigo entender o numero do final')
        else:
            erro = False    
            # oque = 'nada' 
            letras = separarLetra(valor)    
            numeros = separarNumero(valor)  
            valor = sum(map(int, numeros)) + (len(letras)-len(numeros)) 
    else:
        valor = int(valor)

    return chave, valor, erro
        
        


chave, valor, erro = filtrar('x','103xx')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor))

chave, valor, erro = filtrar('x','103x')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor))

chave, valor, erro = filtrar('x','103x2')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor))

chave, valor, erro = filtrar('x','8')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor))

chave, valor, erro = filtrar('x', '8a')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor))

chave, valor, erro = filtrar('x', '8ax')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor))
