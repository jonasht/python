import json

def add_venda(dados_produto, dados_cliente, total): # em dev 
    dados_produtojson = json.dump(dados_produto)
    print('===========================================================')
    print('dados_produto:', dados_produto)
    print('dados_cliente:', dados_cliente)
    print('total:', total)

def add_entregas(entregas): # em dev 
    print('entregas:', entregas)


if __name__ == '__main__':
    dados_produto = [
        ['algo1', 'dados2', 'dados3'],
        ['algo1', 'dados2', 'dados3'],
        ['algo1', 'dados2', 'dados3'],
        ['algo1', 'dados2', 'dados3']
        ]
    
    add_venda(dados_cliente=None,
              dados_produto=dados_produto, 
              total=200.5)
              