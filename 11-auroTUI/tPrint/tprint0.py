red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red


def tprint(*palavras, bg=bgBlue ,op=0):
    
    
    if op == 0:

        print(bg, end='')
        for palavra in palavras:
            print(f"{' '*2}{palavra:^5}{(' '*2):^2}{f}")
        print(f, end='')

print('\n')
tprint('=-'*15+'=')
tprint('primeira palavra')
tprint('segundo palavra')
tprint('terceira palavra')
tprint('=-'*15+'=')
print('\n')
tprint(op=0)