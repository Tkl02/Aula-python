# Uso para testar modificaçoes nos coodigos separadamente

from bs4 import BeautifulSoup
import requests
import pandas as pd

html = pd.read_html('https://www.uol.com.br/esporte/futebol/')
