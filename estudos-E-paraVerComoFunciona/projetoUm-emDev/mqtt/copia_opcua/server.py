from opcua import Server
from uteis import *

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
pessoas = get_dados()

while True:

    input()
    
    for pessoa in pessoas:
        for d in pessoa:
            Dados.set_value(d)
            sleep(0.1)
        print('linha')
        Dados.set_value('linha')
        sleep(0.1)
            
    Dados.set_value('fim')
    sleep(0.1)

