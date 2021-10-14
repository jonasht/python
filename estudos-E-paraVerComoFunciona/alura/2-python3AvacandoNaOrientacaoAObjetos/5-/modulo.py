

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
    
    def imprimir(self):
        print(f'nome: {self._nome} - ano: {self.ano} - likes: {self._likes}')




class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def imprimir(self):
        print(f'nome: {self._nome} - ano: {self.ano} - duracao: {self.duracao} - likes: {self._likes}')
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporada = temporadas
        
    def imprimir(self):
        print(f'nome: {self._nome} - ano: {self.ano} - temporada: {self.temporada} - likes: {self._likes}')
        
        
        
vingadores = Filme('vigadores - a guerra', 2020, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

senhorDosAneis = Filme('senhor dos aneis', 2010, 320)


[senhorDosAneis.dar_like() for _ in range(10)]


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

print('\n=======================================================================')
filmesESeries = [senhorDosAneis, vingadores, gameOf, atlanta]

for programa in filmesESeries:
    programa.imprimir()