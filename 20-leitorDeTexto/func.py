import gtts
from playsound import playsound

def read(txt:list, lang='pt'):
    # se txt = str, txt = list()
    if type(txt) == str: txt = [txt]
    
    for linha in txt:
        frase = gtts.gTTS(linha, lang=lang)
        frase.save('audio.mp3')
        playsound('./audio.mp3')


