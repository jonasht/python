from googletrans import Translator
from colorama.ansi import Fore
def traduzir(texto, src, dest):
    '''
    texto = eh o texto para ser traduzido
    src = DE qual idioma serah traduzido
    dest = PARA qual idioma serah traduzido
    '''
    translator = Translator()
    resultado = translator.translate(texto, src=src, dest=dest)

    # print(resultado.text)
    return resultado.text

if __name__ == '__main__':
    print(Fore.GREEN, end='')
    print(traduzir(texto='ola mundo', src='pt', dest='en'))
    print(Fore.RESET)
