#pegando dados de um site

from bs4 import BeautifulSoup #importa funçao bs4 da biblioteca beutifulsoup que extrai dados HTML e XML
import requests # importa biblioteca request para fazer solicitaçoes HTTP

html = requests.get( #utiliza o request para obter o link e guarda na variavel html
        "https://www.climatempo.com.br/previsao-do-tempo/cidade/1021/morrinhos-go").content # define lik a ser usado na linha anterior em forma de conteudo   

soup = BeautifulSoup(html, 'html.parser') #fazendo uma "traduçao" do codigo HTML e guardando resultado na variavel soup

resumo = soup.find(class_= '-gray -line-height-24 _center') ##buscando conteudo na variavel soup pela classe
tempMin = soup.find(id='min-temp-1')#buscando conteudo na variavel soup pelo id
tempMax = soup.find(id='max-temp-1')#buscando conteudo na variavel soup pelo id

print("Resumo:" + resumo.text)# printando resumo em formato text
print("temp. Minima " + tempMin.string)# printando tempMin em formato string
print("temp. Maxima " + tempMax.string)# printando tempMax em formato string