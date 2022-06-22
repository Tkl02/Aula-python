# PARA FUNCIONAMENTO DO CODIGO:   pip install pyautogui
#                                 pip install BeautifulSoup
#                                 pip install requests


import pyautogui
import time
from bs4 import BeautifulSoup
import requests


id_num = int(input("1-horas -=- 2-temperatura/clima -=- 3-dolar -=- 4-bitcoin: " )) #variavel guarda o valor para continuar processo do IF/else

if id_num == 1: # primeira condiçao (pegando horas)

    html = requests.get('https://www.horario-brasilia.com/').content #usando request para pegar link e guarda na variavel 'html'
    soup = BeautifulSoup(html, 'html.parser') # 'definindo formataçao' de text html na variavel soup
    cvs = soup.find(id='hora') # ele faz a busca por id e guarda na variavel cvs
    print(cvs.string) # printa o resultado da busca 

if id_num == 2: # segunda condiçao (abrindo clima tempo)

    pyautogui.hotkey('win','r') # boton click win + r
    pyautogui.press(['c','h','r','o','m','e']) # didigta chrome
    pyautogui.press('enter') # aperta enter
    time.sleep(1) # pausa de 1 sec
    pyautogui.write("https://www.climatempo.com.br/") # digitando link
    pyautogui.press('enter') # aperta enter

if id_num == 3: # terceira condiçao (cotaçao dolar)

    html = requests.get('https://dolarhoje.com/').content
    soup = BeautifulSoup(html, 'html.parser')
    cvs = soup.find(id='nacional')
    print(cvs['value'])

if id_num ==4: # quarta condiçao (pega dados dos top 10 bitcoins)

    url = "https://coinmarketcap.com/" # guarda link na variavel url 
    result = requests.get(url).text # pega o link em formato de txt e guarna na variavel result
    doc = BeautifulSoup(result, "html.parser") # faz o processo de formataçao de html de codigo da url

    tbody = doc.tbody # definindo tag de uso
    trs = tbody.contents # pegando conteudo da tag

    prices = {}

    for tr in trs[:10]:# criando um laço de execução 
        name, price = tr.contents[2:4] # pegando o nome e o preço do conteudo de tr
        fixed_name = name.p.string # jogando nome em formato string para variavel fixed_name
        fixed_price = price.a.string # jogando preço em formato string para variavel fixed_price

        prices[fixed_name] = fixed_price # formatando nome e preço da criptomoedas
            
    print('\n\n {} \n\n'.format(prices)) # printando resultados

