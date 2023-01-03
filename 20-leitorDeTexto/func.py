import gtts
from playsound import playsound

def read(txt:list):
    # se txt = str, txt = list()
    if type(txt) == str: txt = [txt]
    
    for linha in txt:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('audio.mp3')
        playsound('./audio.mp3')
        # playsound('./musica.mp3')

