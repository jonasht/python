import time
from opcua import Client
from colorama.ansi import Fore
from uteis import *

# ip local do cliente
url = 'opc.tcp://localhost:4840' 

client = Client(url)
client.connect()

print(Fore.GREEN, 'cliente conectado')
print(' client connected ', Fore.RESET)

dadoslista = []
dadosLinhas =[]

while True:

    Dados = client.get_node('ns=2;i=2')
    dados = Dados.get_value()

    if dados == 'linha':
        print('--------------------')
        if dadosLinhas:
            dadoslista.append(list(dadosLinhas))
            dadosLinhas.clear()
    elif dados == 'fim':
        if dadoslista:
     
            u.mostrarMatriz(dadoslista)
            dadoslista.clear()
        continue
    else:
        if str(dados) != '0':
            dadosLinhas.append(dados)

    
    time.sleep(0.1)