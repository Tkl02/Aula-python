from gtts import gTTS             #bibliotecas
from playsound import playsound
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

text = str(input("qual a frase? "))  #variavel para selecionar texto
idioma = str(input("qual idioma"))   #variavel para selecionar idioma

audio = 'meusom.mp3'   #atribuindo nome para o audio

convers = gTTS (       #convertendo o codigo para audio
    text,              #recebendo valor do input text
    lang = idioma      #lang(traduzir) recebendo idioma
)
convers.save(audio)    #salvando codigo com o nome da variavel audio