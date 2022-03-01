#Exercicio 3: fAÇA UM PROGRAMA QUE LEIA UM NUMERO E MOSTRE O SEU SUCESSOR E O ANTECESSOR

from tokenize import Double


n1 = int(input('digite um valor: '))

ant = n1 - 1
sec = n1 + 1

print('o antecessor do numero e: {}, e o sucessor e: {}'.format(ant, sec))

#Exercicio 4: crie um algoritimo que mostre o seu dobro, triplo e sua raiz quadrada

num = float(input('digite um numero:' ))

dobro = num*2   
triplo = num*3
raiz = num**(1/2)

print('o dobro do valor e: {} \n o triplo do valor e: {} \n a raiz do valor e: {}'.format(dobro, triplo, raiz))

#Exercicio 5: some as notas de um aluno e calcule a media

b1 = int(input('nota do primeiro bimestre ?'))
b2 = int(input('nota do segundo bimestre ?'))
b3 = int(input('nota do terceiro bimestre ?'))
b4 = int(input('nota do quarto bimestre ?'))

media = (b1 + b2 + b3 + b4)/4

print('a media do aluno e: ', media)

#Exercicio 6: escreva um algoritimo que converte metros em centimetros e milimetros

metro = float(input('digite o valor em metro: '))

cm = metro * 100
mm = metro * 1000

print('{} metros da {} centimetros e {} milimetros'.format(metro, cm, mm))


#Exercicio 7: faça um algoritmo que leia um numero e mostre sua tabuada

n = int(input('digite um valor: '))

v1 = n*1
v2 = n*2
v3 = n*3
v4 = n*4
v5 = n*5
v6 = n*6
v7 = n*7
v8 = n*8
v9 = n*9
v10 = n*10

print(' {}x1={}  {}x2={}  {}x3={} \n {}x4={}  {}x5={}  {}x6={} \n {}x7={}  {}x8={}  {}x9-{} \n {}x10={}'.format(n, v1, n, v2, n, v3, n, v4, n, v5, n, v6, n, v7, n, v8, n, v9, n, v10))

#Exercicio 8: faça um programa que converta real em dolar

real = float(input('quantos reais deseja converter? '))

dolar = real / 5.16

print('vc tem {:.2f} dolares'.format(dolar))

#Exercico 9: faça um programa que leia a altura e largura de uma parede, mostre a sua area
# e a quantidade necessaria para pintar sabendo que 1L correponde a 2m²

altura = float(input('qual a altura da parede? '))
largura = float (input('qual a largura da parede?'))

area = largura * altura
tinta = area / 2

print('altura : {:.3F} largura : {.3f} area : {:.4f}, serão necessario {:.2f} litros de tinta'.format(altura, largura, area, tinta))

#Exercicio 10: leia o valor de um produto e mostre 5% de desconto

valor = float(input('qual o valor do produto ? '))

desconto = valor * 0.95

print('o valor com o desconto e igual a: {:.2f}'.format(desconto))

#Exercicio 11: leia o valor do salario de um funcionario e mostre-o com um almento de 15%

salario = float(input('qual o salario antigo ? '))

partesalario = salario * 0.15

novosalario = partesalario + salario

print('ganho de {:.2f} reais, valor total : {:.2f} reais'.format(partesalario, novosalario))