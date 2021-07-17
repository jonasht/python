# importando colorama, no linux funciona sem colorama as cores
# no windows funciona com colorama porque nao usa ANSI
import colorama
colorama.init()

# definindo as variaveis das cores fg
fim = '\033[0m'
black = '\033[30m'
red = '\033[31m' 
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m' 
pink = '\033[35m' 
white = '\033[97m'
