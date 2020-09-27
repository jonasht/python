from time import sleep

def txt(palavras):
    for palavra in palavras:
        print(palavra)
        sleep(.09)
    
mensagem =  'lá está esta mensagem '

txt(mensagem)
print(10*'=-=-')
def txt1(palavras):
    for palavra in palavras:
        if palavra == ' ':
            print('')
        else:
            print(palavra, end='')
        
        sleep(.09)
txt1(mensagem)