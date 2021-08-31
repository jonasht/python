import time
from opcua import Client
from colorama.ansi import Fore
from os import system

url = 'opc.tcp://localhost:4840' 

client = Client(url)
client.connect()


mensagemAntiga = ''
while True:
    
    dados = client.get_node('ns=2;i=4')
    mensagem = dados.get_value()
    print(mensagem)
    time.sleep(1)
  
    