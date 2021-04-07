r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
y = '\033[33m' # yellow
f = '\33[m'

bb = '\033[44m' # backgournd blue

def tela(mensagem, colunatxt=5):
    espaco = bb + ' ' + f
    mensagem = bb + y + mensagem 
    for i in range(12):
        print('')
        if i == 5:
                
            print(espaco * colunatxt + mensagem + espaco*(50 - (len(mensagem)-colunatxt)), end='')            
        else:
            for ii in range(50):
                print(espaco, end='')

    print()

tela('aqui tem uma mensagem escrita')