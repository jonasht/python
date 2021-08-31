from datetime import datetime
from opcua import Server
from random import randint
import time 
from colorama.ansi import Fore
import uteis as u

server = Server()

url = 'opc.tcp://localhost:4840' 

server.set_endpoint(url)

name = 'OPCUA_SIMULATION_SERVER'
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Dados = Param.add_variable(addspace, 'Dados', 0)


Dados.set_writable()

# começando servidor
server.start()

print(f'servidor funcionando em {url}')
print(Fore.GREEN + 'funcionando', Fore.RESET)
pessoas = u.get_Pessoas()

while True:

    input()
    
    for pessoa in pessoas:
        for d in pessoa:
            Dados.set_value(d)
            time.sleep(0.1)
        print('linha')
        Dados.set_value('linha')
        time.sleep(0.1)
            
    Dados.set_value('fim')
    time.sleep(0.1)

