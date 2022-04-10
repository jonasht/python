import gtts
from playsound import playsound


with open('frase.txt', 'r') as arq:
    for linha in arq:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase.mp3')
        playsound('./frase.mp3')

