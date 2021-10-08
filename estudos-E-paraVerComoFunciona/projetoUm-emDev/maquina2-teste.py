from maquina import Maquina
from servidorPOO import Servidor

maquina2 = Maquina('maquina2')
maquina2.set_data(variableName='testeFloat', type='float', value=60.2)
servidor = Servidor(maquina2.nomeMaquina)
servidor.dados = maquina2.get_data()
servidor.start()
