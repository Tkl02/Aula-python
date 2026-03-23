#Exercicio 1:Escreva um programa que faça o computador "pensar" em um número inteiro entre O e 5 peça para ousuário tentar 
# dascobrir qual foi o número ascolhido palo computador. O programa davará escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint


num = int(input('tente adivinha um o numero de 0 a 5: '))
numaleatorio = randint(0, 5)
if num == numaleatorio:
    print('parabens voce acertou o numero correto: {}.'.format(numaleatorio))
else:
    print('infelizmente voce errou, o correto e o numero: {}.'.format(numaleatorio))

#Exercicio 2: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h. 
# mostra uma mensagem dizendo que ele foi multado. A multa vai custar RS7.00 por cada Km acima do limite.

velocidade = int(input('qual a velocidade percorrida? '))
if velocidade > 80:
    multa = 7*(velocidade-80)
    print('voce exedeu o limite maximo pague uma multa de: {}R$'.format(multa))
else:
    print('voce não exedeu o limite, continue assim.')

#Exercicio 3: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('digite um numero inteiro: '))
if num%2 == 0:
    print('o numero {} e Par'.format(num))
else:
    print('o numero {} e Impar'.format(num)) 

#Exercicio 4: Dasenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagam. 
# cobrando RS0.50 por Km para viagans de até 200Km e RS0.45 para viagans mais longas.

km = int(input('quantos KMs tem sua viagem? '))
if km <= 200:
    valor = km*0.50
    print('sua viagem deu {:.2f}R$.'.format(valor))
else:
    valor = km*0.45
    print('sua viagem deu {:.2f}R$.'.format(valor))

#Exercicio 5: Faça um programa que leia um ano qualquer e mostre se ale é BISSEXTO.

ano = int(input('qual o ano que deseja analisar? '))
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} e bissexto.'.format(ano))
else:
    print('o ano {} não e bissexto.'.format(ano))

#Exercicio 6:Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero: '))

print('-=-'*9)
print('ANALISANDO...')
print('-=-'*9)

sleep(2.2)

if n1 < n2 and n1 < n3:
    print('o menor numero e: ', n1)
if n2 < n1 and n2 < n3:
    print('o menor numero e: ', n2)
if n3 < n1 and n3 < n2:
    print('o menor numero e: ', n3)
if n1 > n2 and n1 > n3:
    print('o maior numero e: ', n1)
if n2 > n1 and n2 > n3:
    print('o maior numero e: ', n2)
if n3 > n1 and n3 > n2:
    print('o maior numero e: ', n3)


#Exercicio 7: Escreva um programa que pargunta o salário de um Funcionário e calcule o valor do seu aumento.
# Para salários superiores a RS1.250.00. calcula um aumento de 10%. Para os inferiores ou iguais. o aumanto é de 15%.

salario = float(input('qual o seu salario? '))
if salario <= 1250.00:
    aumento = salario+(salario*0.15)
    print('voce ganhou um aumento de 15%, agora recebera: {}R$'.format(aumento))
else:
    aumento = salario+(salario*0.10)
    print('voce ganhou um aumento de 10%, agora recebera: {}R$'.format(aumento))

#Exercicio 8: Dasenvolva um programa que leia o comprimento de três retas a diga ao usuário se elas podem ou nÃo formar um triângulo.

print('-=-'*10)
print('    analisar o trinagulo')
print('-=-'*10)
sleep(1)

r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))

print('-=-'*10)
print('         ANALISANDO...')
print('-=-'*10)

sleep(1.8)

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('e possivel fazer um triangulo')
else:
    print('e impossivel fazer um triangulo')
