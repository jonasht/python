from fCards import Fcards



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
    alternativas = fcards.get_alternativa()
    print('alternativas:', ' '.join(alternativas))

    n = int(input('n: '))

    print('alternativas[n]:', alternativas[n])


    print('certo' if fcards.set_resposta(alternativas[n]) else 'errado')
