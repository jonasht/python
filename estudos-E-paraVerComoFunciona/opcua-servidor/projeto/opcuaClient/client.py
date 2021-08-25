
import time
from opcua import Client
from colorama.ansi import Fore

url = 'opc.tcp://localhost:4840' 

client = Client(url)
client.connect()

print(Fore.GREEN, 'cliente conectado')
print(' client connected ', Fore.RESET)


while True:
    Temp = client.get_node('ns=2;i=2')
    Temperature = Temp.get_value()
    print(Temperature)
    

    Press = client.get_node('ns=2;i=3')
    Pressure = Press.get_value()
    print(Pressure)
    
    TIME = client.get_node('ns=2;i=4')
    TIME_value = TIME.get_value()
    print(TIME_value)
    
    
    time.sleep(1)