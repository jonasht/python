from time import sleep

r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
y = '\033[33m' # yellow


f = '\33[m'
print(r, '\n este programa foi feito no linux')
def l(): print(g, 40*'=-'+'=')

def txt(palavras, cores = [r, b, g]):
    i = 0
    
    l()
    for palavra in palavras.title():
        print(cores[i] + palavra + f, flush=True, end='')
        sleep(.03)
        i += 1
        if i == len(cores):
            i=0 
    print()
    l()

mensagem = 'lá está esta mensagem escrita em cores'

txt(mensagem)
txt(mensagem, [r, b, g, y])
txt(mensagem + ' com parametros', [r, b, g, y, '\033[35m'])
