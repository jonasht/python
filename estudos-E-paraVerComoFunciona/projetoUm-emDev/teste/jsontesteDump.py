import json

numeros = list(range(20))
print('numeros:', numeros)

nomeArquivo = 'teste.json'

with open(nomeArquivo, 'w') as f_obj:
    json.dump(numeros, f_obj)
    