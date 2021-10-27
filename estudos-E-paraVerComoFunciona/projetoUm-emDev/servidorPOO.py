from opcua import Server

from maquina import Maquina
import opcua_machinesFunc as opMachine
from colorama.ansi import Fore
from time import sleep

class Servidor:
    def __init__(self, nomeMaquina):
        self.nomeMaquina = nomeMaquina
        
        self.server = Server()

        # self.url = 'opc.tcp://localhost:4840' 
        self.url = opMachine.get_url(self.nomeMaquina)
        self.server.set_endpoint(self.url)
        
        # registrando nome
        self.name = 'OPCUA_SIMULATION_SERVER'
        self.addspace = self.server.register_namespace(self.name)

        self.node = self.server.get_objects_node()

        self.Param = self.node.add_object(self.addspace, self.nomeMaquina)

        self.Dados = self.Param.add_variable(self.addspace, 'Dados', 0)


        self.Dados.set_writable()


    def start(self):
        # começando servidor
        self.server.start()

        print(Fore.GREEN + 'funcionando', Fore.RESET)
        print(f'servidor funcionando em {self.url}')


        while True:

            sleep(1)
                    
            self.Dados.set_value(self.dados)
            print(f'mandando dados {self.dados}')
            # print(f'{Fore.GREEN} Mandando dados (servidor){Fore.RESET}')


if __name__ == '__main__':
    maquina1 = Maquina('maquina1')
    maquina1.set_data(variableName='teste', type='int', value=50)
    # maquina1.add_intoDB(url='opc.tcp://localhost:4840')
    servidor = Servidor(maquina1.nomeMaquina)
    print(maquina1.nomeMaquina)
    print(maquina1.get_data())
    print('url:', opMachine.get_url(maquina1.nomeMaquina))
    # servidor.dados = maquina1.get_data()
    # servidor.start()
