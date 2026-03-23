# as colunas representamm fimes
# as linhas representam clientes

#  0 1 2 3 4 5 ... 600
# 0  0 0 0 0 0
# 1  0 0 0 0 0
# 2  0 0 0 0 0
# 3  0 0 0 0 0
# 4  0 0 0 0 0
# 5  0 0 0 0 0
# ...
# 600

# cada cliente assiste 92 filmes
# Elabore um programa que preencha a tabela neste formato

import numpy as np
import random

clientes = 601
filmes = 601
filmes_por_clientes = 92

tabela = np.zeros((clientes, filmes), dtype=int)

for cliente in range(clientes):
    filmes_assistidos = random.sample(range(filmes), filmes_por_clientes)

    for filme in filmes_assistidos:
        tabela[cliente][filme] = 1

print(tabela)

# save file
import pandas as pd

df = pd.DataFrame(tabela)
df.to_csv("clientes_filmes.csv", index=False)

# lista 1: valores (uma lista apenas com numeros que não são zeros)
# lista 2: colunas (uma lista dizendo em qual coluna cada numero da lista 1 estava)
# lista 3: ponteiros de linha ( fala onde cada linha comeca e termina dentro da lista 1)
