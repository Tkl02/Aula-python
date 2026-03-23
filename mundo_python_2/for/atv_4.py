# faça um programa que mostre a taboado do numero que o usuario escolher, só que agora utilizando um laço for

numero = int(input('Digite um numero: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')