
import time
from opcua import Client
from colorama.ansi import Fore
from os import system
url = 'opc.tcp://localhost:4840' 

client = Client(url)
client.connect()

print(Fore.GREEN, 'cliente conectado')
print(' client connected ', Fore.RESET)

mensagemAntiga = ''
while True:
    Temp = client.get_node('ns=2;i=2')
    Temperature = Temp.get_value()
    

    Press = client.get_node('ns=2;i=3')
    Pressure = Press.get_value()
    
    # TIME = client.get_node('ns=2;i=4')
    # TIME_value = TIME.get_value()

    # print(Temperature)
    # print(Pressure)

    # print(TIME_value)
    print(Fore.GREEN+'=-'*30+'='+Fore.RESET)
    print(f'temperatura:{Temperature} | pressao {Pressure}')
    
    msg = client.get_node('ns=2;i=4')
    mensagem = msg.get_value()
    
    if mensagem == mensagemAntiga:
        print(f'{Fore.BLUE}mensagem: {Fore.RESET}')
        
    else:
        
        print(f'{Fore.BLUE}mensagem:{Fore.RESET} ', end='')
        print(Fore.GREEN, end='')
        for m in mensagem:
            time.sleep(0.05)
            print(m, end='',flush=True)
        print(Fore.RESET)
        
    mensagemAntiga = mensagem
    
    time.sleep(3)
    system('clear')
    