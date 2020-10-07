

começo_da_frase = 'em dinheiro '
fim_da_frase = "________ reais"
espaço = len(começo_da_frase)*" "

print(espaço, fim_da_frase, "\r", começo_da_frase, flush=True, end="")
valor = input('') 
print(f'o que foi digitado: {valor}')