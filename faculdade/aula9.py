# leitura de streamers

import pyautogui
import time
import string
from turtle import title
from bs4 import BeautifulSoup
import requests

id_num = int(input("1-horas -=- 2-temperatura/clima -=- 4-dolar" ))

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

if id_num == 4:
    