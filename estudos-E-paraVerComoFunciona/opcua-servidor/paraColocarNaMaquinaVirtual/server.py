from datetime import datetime
from opcua import Server
from random import randint
import time 
from colorama.ansi import Fore

server = Server()

url = 'opc.tcp://192.168.15.128/24:4840' 

server.set_endpoint(url)

name = 'OPCUA_SIMULATION_SERVER'
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, 'Time', 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

# começando servidor
server.start()

print(f'server start at {url}')

while True:
    Temperature = randint(10, 50)
    Pressure = randint(200, 900)
    TIME = datetime.now()
    print(Temperature, Pressure, TIME, Fore.GREEN,'funcionando', Fore.RESET)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(2)