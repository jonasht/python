from opcua import Server
from uteis import *
from maquina import Maquina



class Servidor:
    def __init__(self):
        
        self.server = Server()

        self.url = 'opc.tcp://localhost:4840' 



        self.server.set_endpoint(self.url)
        
        
        # registrando nome
        self.name = 'OPCUA_SIMULATION_SERVER'
        self.addspace = self.server.register_namespace(self.name)

        self.node = self.server.get_objects_node()

        self.Param = self.node.add_object(self.addspace, "Parameters")

        self.Dados = self.Param.add_variable(self.addspace, 'Dados', 0)


        self.Dados.set_writable()


    def start(self):
        # começando servidor
        self.server.start()

        print(Fore.GREEN + 'funcionando', Fore.RESET)
        print(f'servidor funcionando em {self.url}')


        while True:

            sleep(.5)
                    
            self.Dados.set_value(self.dados)
            print(f'mandando dados {self.dados}')
            # print(f'{Fore.GREEN} Mandando dados (servidor){Fore.RESET}')


if __name__ == '__main__':
    maquina = Maquina('maquina')
    maquina.set_data(variableName='teste', type='int', value=50)
    servidor = Servidor()
    servidor.dados = maquina.get_data()
    servidor.start()
