#leitor de audio

from gtts import gTTS

from playsound import playsound

audio = 'meusom.mp3'
idioma = 'pt-br'

convers = gTTS (
    text = 'aqui nois mata onça memo',
    lang = idioma
)
convers.save(audio)