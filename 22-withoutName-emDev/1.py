from random import shuffle, choice, sample
perguntasDic = {
    '1+1':'2',
    '1+2':'3',
    '1+3':'4',
    '1+4':'5',
    '1+5':'6',
}
    # '1+6':'7',
    # '1+7':'8',
    # '1+8':'9'


class Fcards:
    def __init__(self, perguntasDic) -> None:
        self.perguntasDic = perguntasDic
        self.perguntas = list(self.perguntasDic.keys()) 
        self.respostas = list(self.perguntasDic.values())

        self.perguntasShuffle = self.perguntas
        
    def start(self):
        shuffle(self.perguntasShuffle)

    def get_pergunta(self):
        # return choice(self.perguntasShuffle)
        return self.perguntasShuffle[0]
        
    def get_alternativa(self):
        perguntaAtual = self.perguntasShuffle[0]
        resposta = self.perguntasDic[perguntaAtual]

        alternativas = list()
        alternativas = sample(self.respostas, 2)
        alternativas.append(resposta)
        shuffle(alternativas)

        return alternativas


        
if __name__ == '__main__':
    fcards = Fcards(perguntasDic=perguntasDic)
    fcards.start()
    print('perguntas embara:', fcards.perguntasShuffle)
    print(fcards.get_pergunta())
    
    print(fcards.get_alternativa())
    