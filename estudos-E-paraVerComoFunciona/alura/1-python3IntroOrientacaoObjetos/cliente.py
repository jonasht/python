class Cliente:
    def __init__(self, nome) -> None:
        self.__nome = nome
    
    @property
    def nome(self):
        print('chamando property')
        return self.__nome.title()

    @nome.setter
    def nome(self, novoNome):
        print('chamando setter')
        self.__nome = novoNome