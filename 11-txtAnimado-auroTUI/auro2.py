red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red

palavras=[]
palavrasN= []
def tprint(p='', bg=bgBlue , fg=yellow, op=1):
    palavrasN.append(len(p))
    
    if op == 2:
        palavrasN.append(10)
        palavras.append(bg+fg+'='*max(palavrasN))
            
    
    if op == 1 and p != '':
        palavras.append(bg + fg + p + ' ' * (max(palavrasN) - len(p)))

    if op == 0:
        print(end='')
        
        
        for palavra in palavras:
            print(palavra + f)
        print(f, end='')
        
def tinput(mensagem, bg=bgBlue, fg=yellow):
    entrada = input(bg + fg + mensagem + 3*" " + f)
    return entrada

print('\n')

tprint('=-'* 20, fg=green)

tprint('qual opção voce deseja')
tprint('1 - sacar')
tprint('2 - depositar')
tprint('--' * 20, fg=red)
tprint('3 - fazer conta')
tprint('=-'* 20, fg=green)
tprint(op=0)
#receber = tinput('qual opção:')
#print(f'a opcão "{receber}" foi escolhida')
print('\n')