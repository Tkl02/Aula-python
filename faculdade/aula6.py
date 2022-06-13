import json
import requests

value =  float(input("qual o valor a ser convertido: "))  # lendo um valor e guardando na variavel

url = 'https://economia.awesomeapi.com.br/all/USD-BRL' # guandando um link na variavel 'url'
response = requests.get(url) # pegando os resultados da url 

dolar_value = float(response.json()['USD']['ask']) # pegando valores definido em formato json (ja convertendo em float) e guardando na variavel

r_value = (value * dolar_value) # convertendo USD para BRL

print("R$ {:.2f}".format(r_value)) # printando resultado ja formatado
