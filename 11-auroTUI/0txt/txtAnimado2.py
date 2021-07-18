from time import sleep

r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
f = '\33[m'

def txt(palavras):
    for palavra in palavras:
        print(g, palavra, f, flush=True, end='')#o frush faz imprimir um do lado do outro, sem ele não funciona
        sleep(.09)
    print()
    
mensagem = 'lá está esta mensagem '

txt(mensagem)
