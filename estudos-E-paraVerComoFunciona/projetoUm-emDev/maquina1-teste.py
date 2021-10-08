from maquina import Maquina
from servidorPOO import Servidor



maquina1 = Maquina('maquina1')
maquina1.set_data(variableName='teste', type='int', value=50)
servidor = Servidor(maquina1.nomeMaquina)
servidor.dados = maquina1.get_data()
servidor.start()
