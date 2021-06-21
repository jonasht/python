from uteis import *



chave, valor, erro, frase = filtrar('x','103xx')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor), '\nfrase:', frase)
print()
chave, valor, erro, frase = filtrar('x','103x')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor), '\nfrase:', frase)
print()
chave, valor, erro, frase = filtrar('x','8')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor), '\nfrase:', frase)
print()
chave, valor, erro, frase = filtrar('x', '8a')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor), '\nfrase:', frase)
print()
chave, valor, erro, frase = filtrar('x', '8ax')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor), '\nfrase:', frase)
print()
chave, valor, erro, frase = filtrar('x','103x2')
print('chave:', chave, 'valor:', valor, 'erro:', erro,'\ntipoValor:', type(valor), '\nfrase:', frase)
print()