from deep_translator import GoogleTranslator


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
        
def traduzir(texto, src, target):
    '''
    texto = eh o texto para ser traduzido
    src = DE qual idioma serah traduzido
    target = PARA qual idioma serah traduzido
    '''
    resultado = GoogleTranslator(source=src, target=target).translate(texto)
    return resultado

if __name__ == '__main__':
    print(traduzir(texto='ola mundo', src='pt', target='en'))

