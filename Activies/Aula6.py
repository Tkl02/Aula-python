#Exercicio 1: Cria um programa que leia o nome completo de uma passoa e mostre:
#a)  O nome com todas as letras maiúsculas
#b)  O nome com todas minúsculas.
#c) Quantas letras ao todo (sem considerar espaços)
#d) quantas letras tem o primeio nome

nome = str(input('qual o seu nome completo? ')).strip()
print('seu nome em maiusculo e: {}'.format(nome.upper()))
print('seu nome em minusculo e: {}'.format(nome.lower()))
print('seu nome e {} e ele tem {} letra'.format(nome, len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras: '.format(nome.find(' ')))

#Exercicio 2: Fasa um programa que leia um número de O a 9999 e mostre na tela cada um dos digitos separados.

num = int(input('digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

#Exercicio 3: Crie um programa que leia o nome de um cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('qual a sua cidade? ')).strip()
print(cidade[:5].upper() == 'SANTO')

#Exercicio 4: Crie um programa que leia o nome de uma passoa e diga se ela tem "SILVA" no nome.

nome = input('voce tem silva em seu nome? digite-o para sabe: ')
print('silva' in nome.lower())

#Exercicio 5: Fasa um programa que leia uma frase palo teclado e mostre: 
# Quantas vezas aparaca a latra "A".
# Em que posição ela aparece na primeira vez. Em que posisão ela aparace na última vez.

frase = str(input('digite uma frase: ')).lower().strip()
print('a letra a aparece: {} vezes'.format(frase.count('a')))
print('a primeira letra a aparece na posição: {}. \ne a ultima na posição: {}.'.format(frase.find('a')+1, frase.rfind('a')+1))

#Exercicio 6: Faça um programa que leia o nome completo de uma passoa e mostre primeiro e o ultimo nome separadamante.

nome = input('qual o seu nome completo ? ').strip()
lista = nome.split()
print('seu primeiro nome e: {}'.format(lista[0]))
print('seu ultimo nome e: {}'.format(lista[len(lista)-1]))
