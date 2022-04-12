import gtts
import gtts.langs
from playsound import playsound

def speak():
    with open('frase.txt', 'r') as arq:
        for linha in arq:
            # frase = gtts.gTTS(linha, lang='pt-br')
            frase = gtts.gTTS(linha, lang='pt-br')
            frase.save('fraseTeste.mp3')
            playsound('./fraseTeste.mp3')
            playsound('./musica.mp3')
            

speak()