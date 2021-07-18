from time import sleep

r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
f = '\33[m'

print('\n este programa foi feito no linux')
def l(): print(40*'=-'+'=')

def txt(palavras):
    i = 0
    cores = [r, b, g]
    l()
    for palavra in palavras.title():
        print(cores[i] + palavra, f, flush=True, end='')
        sleep(.06)
        i += 1
        if i == 3:
            i=0 
    print()
    l()
    
mensagem = 'lá está esta mensagem escrita em cores'

txt(mensagem)
