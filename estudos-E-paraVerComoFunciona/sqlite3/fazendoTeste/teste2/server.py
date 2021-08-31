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


Comando = Param.add_variable(addspace, "Comando", 0)
Titulo= Param.add_variable(addspace, "Titulo", 0)
Dados = Param.add_variable(addspace, 'Dados', 0)

Comando.set_writable()
Titulo.set_writable()
Dados.set_writable()

# começando servidor
server.start()

print(f'servidor funcionando em {url}')
pessoas = u.get_Pessoas()
comando = ''
titulo = 'titulo'

while True:

    # Temp.set_value(Temperature)
    # Press.set_value(Pressure)
    input()
    
    for pessoa in pessoas:
        for d in pessoa:
            Titulo.set_value(titulo)
            Dados.set_value(d)
            print(comando, titulo, d)
            time.sleep(1)
        print('linha')
        Dados.set_value('linha')
        time.sleep(1)
            


