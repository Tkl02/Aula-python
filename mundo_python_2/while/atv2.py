# faça um sorteio que voce dara palpites ate que acerto o numero e mostre quantos palpites foram feitos

import random
count = 0
palpite = ""
num = random.randint(0,10)
print(f"---\n{num}\n---")
while palpite != num:
    palpite = int(input("adivinhe o numero: "))
    count += 1

print(f"voce deu palpite {count} para acertar")