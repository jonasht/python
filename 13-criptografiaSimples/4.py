# feito no linux


# foregrounds

color = {
    'black': '\033[30m',
    'red': '\033[31m' ,
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    }

f = '\33[m'

# backgrounds
bgColor = {
        'Black': '\033[40m',
        'Red': '\033[41m' ,
        'Green': '\033[42m',
        'Yellow' :'\033[43m',
        'Blue': '\033[44m',
        'Magenta': '\033[45m',
        'Cyan': '\033[46m',
        'White': '\033[47m',
}
palavras = []
palavrasN = []
tipo = []

def tprint(p='', bg=bgColor['White'] , fg=color['green'], op=1, tamanhoDaPalavra=0):
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
        del(palavras[:])
        #del(palavrasN[:])
        del(tipo[:])
        

tprint('/', op=2)
tprint(op=2)
tprint(tamanhoDaPalavra=30)
tprint('mensagem para ser criptografada:'.upper())
tprint(op=0)
mensagem = input()


letras = []


letras.extend(mensagem)
cletras = []
for letra in letras:
    cletras.append(chr(ord(letra)+1))


tprint(mensagem)
tprint('-', op=2)
tprint('mensagem criptada:'.upper())
tprint(''.join(cletras) )
tprint(op=2)
tprint('/', op=2)
tprint(op=0)



