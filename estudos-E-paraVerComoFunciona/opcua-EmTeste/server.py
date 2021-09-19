from opcua import Server
from random import randint

server = Server()

url = 'opc.tcp://localhost:4840' 

server.set_endpoint(url)

name = 'OPCUA_SIMULATION_SERVER'
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
msg = Param.add_variable(addspace, 'Mensagem', 0)



Temp.set_writable()
Press.set_writable()
msg.set_writable()


# começando servidor
server.start()

print(f'server start at {url}')


while True:
    # fazendo valores de temperatura e pressao
    Temperature = randint(10, 50)
    Pressure = randint(200, 1000)
    
    
    print(Temperature, Pressure)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    
    
    mensagem = input('qual eh a mesagem:')
    msg.set_value(mensagem)

