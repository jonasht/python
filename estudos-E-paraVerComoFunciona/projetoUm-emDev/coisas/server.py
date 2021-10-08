from opcua import Server
from uteis import *

server = Server()

# url = 'opc.tcp://localhost:4840' 
url = 'opc.tcp://localhost' 


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





pessoas = get_data()
while True:

    for pessoa in pessoas:
        dados = ''
        for dado in pessoa:
            dados += f'{dado} '
        sleep(.1)
            
        Dados.set_value(dados)
        print(f'{Fore.GREEN} Mandando dados (servidor){Fore.RESET}')


