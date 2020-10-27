mensagem = 'esta eh uma mensagem'


letras = []
print(f'\nmensagem a ser criptada:\n {mensagem}')

letras.extend(mensagem)
cletras = []
for letra in letras:
    cletras.append(chr(ord(letra)+1))
print('\nmensgem criptada:')
for cletra in cletras:
    print(cletra, end='')