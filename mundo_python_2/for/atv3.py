# faça um programa que calcula a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 a 500

soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i   
print(soma)