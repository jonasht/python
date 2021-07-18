import requests

url = 'https://api.exchangerate-api.com/v6/latest'
requisicao = requests.get(url)


print(requisicao.status_code)
dados = requisicao.json()
print(dados)
print('='*30)

valorEmReais = float(input('para converter, informe o valor em R$:'))
cotacao = dados['rates']['BRL']
print(f'R${valorEmReais} reais são U$: {(valorEmReais / cotacao):.2f}')