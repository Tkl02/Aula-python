# faça uma contador infinito de homes e mulheres de uma lista usando while
man = woman = 0
while True:
    sexo = input("Sexo? (M/F) ").upper()

    if sexo == 'M':
        man += 1
    elif sexo == 'F':
        woman += 1
    else:
        break

print(f"Quantidade de homens: {man}, quantidade de mulheres: {woman}")
