# faça um contador regressivo de 10 a 0 com pausa de 1 segundo entre eles

import time
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
    if i == 0:
        print('FIM')