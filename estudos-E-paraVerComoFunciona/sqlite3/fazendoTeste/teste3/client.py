
import time
from opcua import Client
from colorama.ansi import Fore

url = 'opc.tcp://localhost:4840' 

client = Client(url)
client.connect()

print(Fore.GREEN, 'cliente conectado')
print(' client connected ', Fore.RESET)

dadoslista = []
dadosLinhas =[]
while True:
    Comando = client.get_node('ns=2;i=2')
    comando = Comando.get_value()

    Titulo = client.get_node('ns=2;i=3')
    titulo = Titulo.get_value()
    # p
    
    Dados = client.get_node('ns=2;i=4')
    dados = Dados.get_value()

            
        
    if dados == 'linha':
        print('linha --------------------')
        if dadosLinhas:
            dadoslista.append(list(dadosLinhas))
            dadosLinhas.clear()
    elif dados == 'fim':
        if dadoslista:
            print(dadoslista)
            dadoslista.clear()
        continue
    else:
        if str(dados) != '0':
            print(f'{dados} ', end='')
            dadosLinhas.append(dados)

    
    time.sleep(1)
    