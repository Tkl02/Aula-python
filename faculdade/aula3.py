#leitor de audio

from gtts import gTTS

from playsound import playsound

a = str(input('digite a frase: '))

audio = 'meusom.mp3'
idioma = 'pt-br'

convers = gTTS (
    text = (a),
    lang = idioma
)
convers.save(audio)