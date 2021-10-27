class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporada = temporadas
        

        
        
vingadores = Filme('vigadores - a guerra', 2020, 160)
vingadores.dar_like()
print(f'nome: {vingadores.nome} - ano: {vingadores.ano} - duracao: {vingadores.duracao}')
print(f'likes: {vingadores.likes}')

gameOf = Serie('game of thrones', 2010, 9)
print(f'Nome: {gameOf.nome} - ano: {gameOf.ano} - temporadas: {gameOf.temporada}')
gameOf.dar_like()
print(vingadores.nome)


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')

print('======================================================')
filmesESeries = [vingadores, gameOf, atlanta]

for programa in filmesESeries:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada

    print(f'\t{programa.nome} - {detalhes} - {programa.likes}')
