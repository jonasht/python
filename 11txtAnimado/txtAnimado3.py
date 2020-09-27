from time import sleep

r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
f = '\33[m'


def txt(palavras):
    i = 0
    cores = [r, b, g]
    for palavra in palavras:
        print(cores[i], palavra, f, flush=True, end='')
        sleep(.09)
        i += 1
        
        if i == 3:
            i=0
            
    print()
    
mensagem = 'lá está esta mensagem '

txt(mensagem)
