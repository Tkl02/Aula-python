#Exercício Python 2: Faça um programa que leia algo pelo teclado e 
#                    mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input('digite algo: ')
print('tipo primitivo e: ', type(palavra))
print('E somente espaços', palavra.isspace())
print('E somente numeros ?', palavra.isnumeric())
print('Ele e alfabetico ?', palavra.isalpha())
print('Ele e alfanumerico?', palavra.isalnum())
print('Ele esta somente em maiuscula?', palavra.isupper())
print('Ele esta somente em minuscula ?', palavra.islower())
print('Ele esta catalizada?', palavra.istitle())