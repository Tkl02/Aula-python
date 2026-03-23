# calcule o fatorial de um numero

num = int(input("Digite um número: "))
resultado_fatorial = 1

while num != 0:
    resultado_fatorial *= num
    num -= 1

print(f"O fatorial é: {resultado_fatorial}")
