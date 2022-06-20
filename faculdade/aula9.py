# leitura de streamers


from bs4 import BeautifulSoup
import requests



#id_num = int(input("1-valorant -=- 2-league of legends -=- 3- Counter Strink go"))

#if id_num == 1:

html = requests.get('https://www.twitch.tv/directory/game/VALORANT').content

soup = BeautifulSoup(html, 'html.parser')

titulo1 = soup.find('title')
nome1 = soup.find(class_='CoreText-sc-cpl358-0 eyuUlK')

print(titulo1.string)
print(nome1)



#if id_num == 2:

#if id_num == 3:
