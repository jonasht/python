import json


nomeArquivo = 'teste.json'

with open(nomeArquivo) as f:
    numeros = json.load(f)

print(numeros)