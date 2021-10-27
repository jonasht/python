from maquina import Maquina
from servidorPOO import Servidor
import opcua_machinesFunc as opMachine


maquina2 = Maquina('maquina2')
maquina2.set_data(variableName='teste', type='int', value=85)

# opMachine.add_(name=maquina2.nomeMaquina, ip='localhost', url='opc.tcp://localhost:4840')
servidor = Servidor(maquina2.nomeMaquina)
# print(maquina2.nomeMaquina)
# # print(maquina2.get_data())
print('url:', opMachine.get_url(maquina2.nomeMaquina))
servidor.dados = maquina2.get_data()
servidor.start()
