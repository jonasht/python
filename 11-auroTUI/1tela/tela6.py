red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red

def tela(mensagens, colunatxt=5, qtdLinhas = 10, bg=bgYellow, fg = green):
    espaco = bg + ' ' + f

    for i in range(qtdLinhas-len(mensagens)): 
        print('')
        if i == 2:
            for mensagem in mensagens: 
                mensagem = bg + fg + mensagem
                print(espaco * colunatxt + mensagem + espaco*(50 - (len(mensagem)-colunatxt)),)
        print(espaco*50, end='')

    

tela(['aqui tem uma mensagem escrita', 
      'esta é outra mensagem',
       'outra aqui',
       'eu estou escrevendo outro texto'])

tela(['eu estou escrevendo mais um texto',
    'aqui tem uma mensagem escrita', 
      'esta é outra mensagem',
       'outra aqui', 
       'eu estou escrevendo outro texto'], fg=blue)

tela(['eu estou escrevendo mais um texto',
    'aqui tem uma mensagem escrita', 
      'esta é outra mensagem',
       'outra aqui', 
       'eu estou escrevendo outro texto'], fg=red)

print()