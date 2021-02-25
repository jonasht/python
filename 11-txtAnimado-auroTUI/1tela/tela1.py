r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
y = '\033[33m' # yellow
f = '\33[m'

bb = '\033[44m' # backgournd blue
def tela(mensagem):
    for i in range(12):
        print('')
        for ii in range(50):
            print(f'{bb} ', end='')
            if ii == 5 and i == 5:
                print(y, mensagem, end='')
    print(f)

tela('Esta daqui é uma frase')
