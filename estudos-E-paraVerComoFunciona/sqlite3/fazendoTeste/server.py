from sqlite3.dbapi2 import paramstyle
from opcua import Server
import uteis as v
import time


server = Server()

url = 'opc.tcp://localhost:4840' 

server.set_endpoint(url)

name = 'OPCUA_SIMULATION_SERVER'
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")
Comando = Param.add_variable(addspace, 'Comando', 0)

Titulo = Param.add_variable(addspace, 'Titulo', 0) 
Dados = Param.add_variable(addspace, 'Dados', 0)
Comando.set_writable()
Titulo.set_writable()
Dados.set_writable()


# começando servidor
server.start()

print(f'servidor funcionando em{url}')

pessoas = v.get_Pessoas()
while True:
    
    # dados = v.get_Pessoas()
    for pessoa in pessoas:
        for d in pessoas:
            
            Dados.set_value(d)
            print(d)
  
            time.sleep(1)
