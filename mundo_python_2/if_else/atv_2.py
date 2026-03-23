# escreva um programa que leia um numero inteiro e peça para o usuario
# escolher em convertelho para binario, octal, hexadecimal.

num = int(input("digite um numero ? "))
cv = input("Voce deseja converter para 1-binario 2-octal 3-hexadecimal ? ")

if cv == "1" or "binario":
    x = bin(num)
    print(f"seu numero em binario e: {x}")

elif cv == "2" or "octal":
    x = oct(num)
    print(f"seu numero em octal e: {x}")

elif cv == "3" or "hexadecimal":
    x = hex(num)
    print(f"seu numero em hexadecimal e: {x}")

else:
    print("\033[33m parametros invalido verifique e execute novamente\033[m")