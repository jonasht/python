red = '\033[31m' # red
blue = '\033[34m' # blue
green = '\033[32m' # green
yellow = '\033[33m' # yellow
f = '\33[m'

bgBlue = '\033[44m' # backgournd blue
bgYellow = '\033[43m' #backgournd yellow
bgRed = '\033[41m' #backgournd red
# auroReturn
def ar (msn, fg=yellow, bg=bgBlue):
    
    return  bg + fg + ' '+ msn + ' ' + f 

for linha, coluna in ((l, c) for l in range(10) for c in range(10)):
    if coluna == 0: print('')
    print(ar(f'{linha}X{coluna}={linha * coluna} '))

