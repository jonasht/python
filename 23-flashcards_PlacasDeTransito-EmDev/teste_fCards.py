from fCards import Fcards




perguntasDic1 = {
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

perguntasDict = {
    'green': 'verde',
    'yellow': 'amarelo',
    'black': 'preto',
    'blue': 'azul',
    'red': 'vermelho',
    'white': 'branco',
    'one': 'um',
    'two': 'dois',
    }



if __name__ == '__main__':
    # fazendo testes 
    # chamando fcards
    fcards = Fcards(perguntasDic=perguntasDict)
    fcards.start()

    print(fcards.get_pergunta())
    alternativas= fcards.get_alternativa()
    print('alternativas:', ' '.join(alternativas))

    n = int(input('n: '))

    print('alternativas[n]:', alternativas[n])


    print('certo' if fcards.set_resposta(alternativas[n]) else 'errado')
