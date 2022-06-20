from bs4 import BeautifulSoup
import requests

html = requests.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox').content