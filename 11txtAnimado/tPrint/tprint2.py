red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red

palavras=[]

def tprint(p='', bg=bgBlue , fg=yellow, op=1):
    
    if op == 1 and p != '':
        palavras.append(bg+fg+'  '+p+' '*2)
    if op == 2:
        palavras.append(bg+fg+'=-'*15+'=')
    if op == 0:
        print(end='')
        for palavra in palavras:
            print(f"{palavra:^5}{f}")
        print(f, end='')

print('\n')
tprint(op=2)
tprint('primeira palavra')
tprint('segundo palavra')
tprint('terceira palavra', fg=green)
tprint(op=2, fg=red)

tprint(op=0)
print('\n')