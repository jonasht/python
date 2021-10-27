class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporada = temporadas
        


vingadores = Filme('vigadores - a guerra', 2020, 160)


print(f'nome: {vingadores.nome} - ano: {vingadores.ano} - duracao: {vingadores.duracao}')

gameOf = Serie('game of thrones', 2010, 9)
print(f'Nome: {gameOf.nome} - ano: {gameOf.ano} - temporadas: {gameOf.temporada}')