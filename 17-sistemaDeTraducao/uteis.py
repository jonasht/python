from googletrans import Translator
from colorama.ansi import Fore

lang_values = {
    'af': 'africano',
    'ar': 'arabe',
    'eu': 'basco',
    'zh-cn': 'chines (simplificado)',
    'zh-tw': 'chines (traditional)',
    'cs': 'tcheco',
    'en': 'ingles',
    'eo': 'esperanto',
    'de': 'alemao',
    'el': 'greco',
    'it': 'italiano',
    'ja': 'japanese',
    'ko': 'coreano',
    'la': 'latim',
    'pl': 'polones',
    'pt': 'portugues',
    'ru': 'russo',
    'es': 'espanhol',
    'zu': 'zulu'
}
def get_key(dic, value):
    for k, v in dic.items():
        if v == value:
            return k
        
def traduzir(texto, src, dest):
    '''
    texto = eh o texto para ser traduzido
    src = DE qual idioma serah traduzido
    dest = PARA qual idioma serah traduzido
    '''
    translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.com.br',
    ])
    
    resultado = translator.translate(text=texto, src=src, dest=dest)

    # print(resultado.text)
    return resultado.text

if __name__ == '__main__':
    print(Fore.GREEN, end='')
    print(traduzir(texto='ola mundo', src='pt', dest='en'))
    print(Fore.RESET)
