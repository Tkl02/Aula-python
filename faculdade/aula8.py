#pegando dados de um site

from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/2731/joviania-go").content 
        #guardando o link do site na variavel html (content = resgatar conteudo)

soup = BeautifulSoup(html, 'html.parser') #fazendo a converçao de texto para estrutura HTML

result = soup.find(class_= '-gray -line-height-24 _center') #buscando texto pela class

atribut = soup.find(class_='variables-list')
tempMin = soup.find(id='min-temp-1')#busca de temp min pelo ID
tempMax = soup.find(id='max-temp-1')#busca de temp max pelo ID

print(result.text)
print(atribut.text)
print("temperatura min {} max {}.".format(tempMin.string, tempMax.string))