# crie um programa que leia uma frase e diga se ela é um palindromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper() # strip() remove os espaços no inicio e no fim da frase e upper() deixa tudo em maiusculo

palavras = frase.split() # split() separa as palavras da frase e coloca em uma lista

junto = ''.join(palavras) # join() junta as palavras da lista e coloca em uma string

inverso = '' # cria uma string vazia

for letra in range(len(junto) - 1, -1, -1): # len(junto) - 1 é o ultimo indice da string junto, -1 é o indice inicial e -1 é o passo
    inverso += junto[letra] # adiciona as letras da string junto na string inverso de tras para frente

print(f'O inverso de {junto} é {inverso}') # mostra a frase e o inverso dela

if inverso == junto: # se o inverso for igual a frase
    print('Temos um palindromo!') # mostra que é um palindromo