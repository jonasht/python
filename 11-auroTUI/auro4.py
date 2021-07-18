red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red

palavras = []
palavrasN = []
tipo = []

def tprint(p='', bg=bgBlue , fg=yellow, op=1):
    palavrasN.append(len(p))
    
    if op == 2: # enfeite
        tipo.append(2)
        palavras.append(bg + fg + '=')
        
    if op == 1 and p != '': # pohr texto
        tipo.append(1)
        
        palavras.append(bg + fg + ' ' + p + ' ' + ' ' * (max(palavrasN) - len(p)))

    if op == 0: # iniciar 
        print(end='')
        
        
        for i, palavra in enumerate(palavras):
            if tipo[i] == 2:
                print(palavra * (max(palavrasN)+2) + f)
            else:
                print(palavra + f)
        print(f, end='')
        
def tinput(mensagem, bg=bgBlue, fg=yellow):
    fimDaMsg = '____________'
    espaço = len(mensagem) * ' '

    print(bg, fg, espaço + fimDaMsg + "\r" + mensagem, f, flush=True, end="")
    entrada = input('') 
    return entrada

print('\n')


tprint(op=2)
tprint('qual opção voce deseja')
tprint('1 - sacar')
tprint('2 - depositar')
tprint('3 - fazer conta')
tprint(op=2)
tprint(op=0)

#receber = tinput('qual opção:')
#print(f'a opcão "{receber}" foi escolhida')
print('\n')