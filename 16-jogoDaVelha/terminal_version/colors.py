# tentando importar colorama, no linux funciona sem colorama as cores
# no windows funciona com colorama 

try:
    from colorama import init, Fore, Back, Style
except:
    # definindo as variaveis das cores fg
    fim = '\033[0m'
    black = '\033[30m'
    red = '\033[31m' 
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m' 
    pink = '\033[35m' 
    white = '\033[97m'
else:
    init()
    fim = Style.RESET_ALL
    black = Fore.BLACK
    red = Fore.RED
    green = Fore.GREEN
    blue = Fore.BLUE
    white = Fore.WHITE
    yellow = Fore.YELLOW
    cyan = Fore.CYAN
    magenta = Fore.MAGENTA
    lightblack = Fore.LIGHTBLACK_EX
if __name__ == '__main__':
    print('teste')
    print(black, 'black/preto')
    print(red, 'red/vermelho')
    print(green, 'green/verde')
    print(blue, 'blue/azul')
    print(white, 'white/branco')
    print(yellow, 'yellow/amarelo')
    print(cyan, 'cyan/ciano')
    
    print(fim)
    cores = [black, red, green, blue, white, yellow, cyan, magenta, lightblack]

    for c in cores:
        print(c, '0', fim, end='')
    print()
        
        