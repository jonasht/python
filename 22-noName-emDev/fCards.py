from random import shuffle, choice, sample
perguntasDic = {
    '1+1':'2',
    '1+2':'3',
    '1+3':'4',
    '1+4':'5',
    '1+5':'6',
    '1+6':'7',
    '1+7':'8',
    '1+8':'9',
    '6X7':'42'
}


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

    def set_resposta(self, resposta):
        print('=-'*30+'=')
        pergunta = self.perguntasShuffle[0]
        print('r:', pergunta)
        
        if perguntasDic[pergunta] == resposta:
            del(self.perguntasShuffle[0])
            return True
        else:
            r = self.perguntasShuffle.pop(0)
            self.perguntasShuffle.append(r)
            return False

    def working(self) -> bool:
        return True if self.perguntasShuffle else False



        
if __name__ == '__main__': # fazendo testes
    from colorama.ansi import Fore
    from os import system
    
    fcards = Fcards(perguntasDic=perguntasDic)
    fcards.start()
    def l(): # p deixar bonito
        print('=-'*30+'=')
        
    while fcards.working():
        
        l()
        print(fcards.get_pergunta())
        alternativas = fcards.get_alternativa()
        print(Fore.BLUE+'opções:'+Fore.RESET)
        for i, alternativa in enumerate(alternativas):
            print(f'{Fore.BLUE}{i}: {Fore.RESET}{alternativa}')

            
        r = input(': ')
        if r == 's':
            break
        r = int(r)
        system('clear')
        if r > 2 or r < 0:
            print(Fore.RED+'error, somente 0 1 2 sao aceitos'+Fore.RESET)
        else:
            print('correto' 
                  if fcards.set_resposta(alternativas[r])
                  else 'incorreto')
        

    