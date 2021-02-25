red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red
print('\n'*5)
def tinput(mensagem, bg=bgBlue, fg=yellow):
    fimDaMsg = '____________'
    espaço = len(mensagem) * ' '

    print(bg, fg, espaço + fimDaMsg + "\r" + mensagem, f, flush=True, end="")
    entrada = input('') 
    return entrada


receber = tinput('diga algo de bom para o mundo:')

print(f'a opcão "{receber}" foi escolhida')
print('\n')