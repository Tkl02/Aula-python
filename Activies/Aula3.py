#Faça um coodigo que calcule o valor de BASCARA e reproduz seu resultado

import math

a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))

#CALCULANDO DELTA

delta= (b*b) -4 * a * c

#CALCULANDO X¹ E X²

x1 = -b + math.sqrt(delta)/2*a
x2 = -b - math.sqrt(delta)/2*a

print('o valor de delta e: {} o valor de x¹ e: {} o valor de x² e: {}'.format(delta, x1, x2))