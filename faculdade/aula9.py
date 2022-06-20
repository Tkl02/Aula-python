# leitura de streamers


from bs4 import BeautifulSoup
import requests



#id_num = int(input("-=- 1-dolar -=- 2-clima -=-"))

#if id_num == 1:

html = requests.get('https://www.google.com/search?q=dolar+hoje&rlz=1C1FCXM_pt-PTBR994BR994&oq=dolar&aqs=chrome.0.69i59j69i57j69i60l2.3227j0j7&sourceid=chrome&ie=UTF-8').content

soup = BeautifulSoup(html, 'html.parser')

titulo1 = soup.find(class_= 'DFlfde SwHCTb')


print(titulo1)

