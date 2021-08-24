
import time
from opcua import Client
from colorama.ansi import Fore, Back

url = 'opc.tcp://192.168.15.128/24:4840' 

client = Client(url)
client.connect()

print(Fore.GREEN, 'cliente conectado')
print(' client connected ', Fore.RESET)


while True:
    Temp = client.get_node('ns=2;i=2')
    Temperature = Temp.get_value()
    Temperature = Temp.get_value()
    print(Temperature, '', end='')
    

    Press = client.get_node('ns=2;i=3')
    Pressure = Press.get_value()
    print(Pressure, end='')
    
    TIME = client.get_node('ns=2;i=4')
    TIME_value = TIME.get_value()
    print(TIME_value, Back.GREEN, ' ', Back.RESET, '\n')
    
    
    
    
    time.sleep(1)