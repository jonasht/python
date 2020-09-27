from time import sleep

def txt(palavras):
    for palavra in palavras:
        print(palavra, flush=True, end='')#o frush faz imprimir um do lado do outro, sem ele não funciona
        sleep(.09)
    print()
    
mensagem =  'lá está esta mensagem '

txt(mensagem)
