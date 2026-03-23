# escreva um programa que leia 2 numeros e mostre qual desses numero e maior.

num_a = float(input("digite um numero: "))
num_b = float(input("digite um numero: "))

if num_a > num_b:
    print("o primeiro valor e maior.")
elif num_a < num_b:
    print("o segundo valor e maior.")
else:
    print("os valores sao iguai.")