import colorama
colorama.init()

black = '\033[30m' # black
red = '\033[31m' # red
green = '\033[32m' # green
yellow = '\033[33m' # yellow
blue = '\033[34m' # blue
magenta = '\033[35m' #
cyan = '\033[36m' #
white = '\033[37m' #
f = '\33[m'

bgBlack = '\033[40m' # background black
bgRed = '\033[41m' # background red
bgGreen = '\033[42m' # background green
bgYellow = '\033[43m' # background yellow
bgBlue = '\033[44m' # background blue
bgMagenta = '\033[45m' # background magenta
bgCyan = '\033[46m' # backgournd cyan
bgWhite = '\033[47m' # backgroundwhite

palavras = []
palavrasN = []
tipo = []

def tprint(p='', bg=bgWhite , fg=green, op=1, tamanhoDaPalavra=0):
    if tamanhoDaPalavra!= 0: # decidir o tamanho da palavra
        palavrasN.append(tamanhoDaPalavra)
    else:
        palavrasN.append(len(p))
    
    if op == 2: # enfeite
        if p!='':
            tipo.append(2)
            palavras.append(bg + fg + p)            
        else:                   
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
        
mensagem = 'esta eh uma mensagem'

letras = []
print(f'\nmensagem a ser criptada:\n {mensagem}')

letras.extend(mensagem)
cletras = []
for letra in letras:
    cletras.append(chr(ord(letra)+1))

tprint('/', op=2)
tprint(op=2)
tprint(tamanhoDaPalavra=30)
tprint('mensagem para ser criptografada:'.upper())
tprint(mensagem.title())
tprint('-', op=2)
tprint('mensagem criptada:'.upper())
tprint(''.join(cletras) )
tprint(op=2)
tprint('/', op=2)
tprint(op=0)



