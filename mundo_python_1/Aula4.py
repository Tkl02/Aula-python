#Exercicio 1: crie um programa que leia qualquer numero real e mostre seu inteiro

import math

num = float(input('digite um valor qualquer: '))

print('o valor inteiro e: {}'.format(math.trunc(num)))

#Exercicio 2: faça um programa que leia o valor do cateto oposto e adjacente e calcule a hipotenusa

co = float(input('qual o valor do cateto oposto? '))
ca = float(input('qual o valor do cateto adjacente? '))

hp = math.hypot(co, ca)

print('a hipotenusa e: {:.2f}'.format(hp))

#Exercicio 3: crie um programa que leia o angulo e mostre seu seno cosseno e tangente

angulo = int(input('digite o angulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(' o valor de seno e: {:.2f} \n o valor do cosseno : {:.2f} \n o valor da tangente e: {:.2f}'.format(sen, cos, tan))

#Exercicio 4: crie um programa que leia o nome dos alunos em seguida mostre o sorteio entre eles

import random

a1 = str(input('primeiro aluno '))
a2 = str(input('segundo aluno '))
a3 = str(input('terceiro aluno '))
a4 = str(input('quarto aluno '))
a5 = str(input('quinto aluno '))

lista = [a1, a2, a3, a4, a5]

aluno = random.choice(lista)

print('o aluno sorteado foi: {}'.format(aluno))

#Exercicio 5: faça um programa que leia o nome de 5 alunos e ordene de maneira aleatoria


a1 = str(input('primeiro aluno '))
a2 = str(input('segundo aluno '))
a3 = str(input('terceiro aluno '))
a4 = str(input('quarto aluno '))
a5 = str(input('quinto aluno '))

lista = [a1, a2, a3, a4, a5]

random.shuffle(lista)

print('o aluno sorteado foi: {}'.format(lista))
