from opcua import Server


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

print(f'servidor funcionando em{url}')


while True:
    dados = 'funcionando'
    Dados.set_value(dados)

