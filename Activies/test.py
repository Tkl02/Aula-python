# Uso para testar modificaçoes nos coodigos separadamente

from time import sleep


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