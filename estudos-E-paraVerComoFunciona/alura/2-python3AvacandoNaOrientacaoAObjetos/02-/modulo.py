class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporadas
        
        self.__likes = 0

    @property
    def dar_like(self):
        self.__likes += 1
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
        
        
        
vingadores = Filme('vigadores - a guerra', 2020, 160)


print(f'nome: {vingadores.nome} - ano: {vingadores.ano} - duracao: {vingadores.duracao}')

gameOf = Serie('game of thrones', 2010, 9)
print(f'Nome: {gameOf.nome} - ano: {gameOf.ano} - temporadas: {gameOf.temporada}')

print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')