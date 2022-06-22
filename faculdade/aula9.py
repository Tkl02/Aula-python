# PARA FUNCIONAMENTO DO CODIGO:   pip install pyautogui

import pyautogui
import time
from bs4 import BeautifulSoup
import requests

id_num = int(input("1-horas -=- 2-temperatura/clima -=- 3-dolar -=- 4-bitcoin: " ))

if id_num == 1:

    html = requests.get('https://www.horario-brasilia.com/').content
    soup = BeautifulSoup(html, 'html.parser')
    cvs = soup.find(id='hora')
    print(cvs.string)

if id_num == 2:

    pyautogui.hotkey('win','r')
    pyautogui.press(['c','h','r','o','m','e'])
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("https://www.climatempo.com.br/")
    pyautogui.press('enter')

if id_num == 3:

    html = requests.get('https://dolarhoje.com/').content
    soup = BeautifulSoup(html, 'html.parser')
    cvs = soup.find(id='nacional')
    print(cvs['value'])

if id_num ==4:

    result = requests.get('https://coinmarketcap.com/').text
    doc = BeautifulSoup(result, "html.parser")

    tbody = doc.tbody
    trs = tbody.contents

    prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

prices[fixed_name] = fixed_price
    
print('\n\n {} \n\n'.format(prices))
