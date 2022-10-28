# pedra papel tesoura.

import random

jogador =  int(input('''escolha: [0]pedra [1]papel [2]tesoura '''))
pc = random.randint(0,2)
itens = ('pedra','papel','tesoura')

print("\no computado jogo \033[31m{}\033[m".format(itens[pc]))
print("voce escolheu \033[31m{}\033[m".format(itens[jogador]))
 
if pc == 0:
    if jogador == 0:
        print('o jogo empato')
    if jogador == 1:
        print('voce ganho')
    if jogador == 2:
        print('voce perdeu')

if pc == 1:
    if jogador == 0:
        print('voce perdeu')
    if jogador == 1:
        print('o jogo empato')
    if jogador == 2:
        print('voce ganho')

if pc == 2:
    if jogador == 0:
        print('voce ganho')
    if jogador == 1:
        print('voce perdeu')
    if jogador == 2:
        print('o jogo empato')