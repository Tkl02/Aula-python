#Operaçoes com string

# a frase sera dividida em modulos de acordo com seu tamanho, começando no numero 0. 

from posixpath import split


frase = ('aprendendo string em python')
print(frase[8])

# o coodigo mostrara a letra correspondente ao numero de "casa".

frase = ('aprendendo string em python')
print(frase[0:8])

# (primeiro ":"  -> numero "ate" numero)  (segundo ":" pular casas)

frase = ('aprendendo string em python')
print(frase[0:8:2])

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
# o comando count conta quantas letras tem repetidas (lembrando que "O" maiusculo é ≠ "o" minusculo)

frase = ('Aprendendo String usando Python')
print(frase.count('a'))

#para a opçao acima funcionar dever-se igualar as letras usando "upper" ou "lower"

frase = ('Aprendendo String usando Python')
print(frase.upper().count('A'))
#             ↑            ↑  eles devem corresponder

frase = ('Aprendendo String usando Python')
print(frase.lower().count('A'))
#             ↑            ↑  eles devem corresponder

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# a função "len" indica a quantidade de modulos presente na frase, espaços adiciona mais "casa"

frase = ('Aprendendo String usando Python')
print(len(frase))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# a função strip remove espaços indesejados da frase

frase = ('             Aprendendo String usando Python              ')
print(len(frase))

frase = ('             Aprendendo String usando Python              ')
print(len(frase.strip()))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# a função "replace" troca uma palavra pela outra mas FORA DA STRING.
# as palavras devem ser exatamente iguais, levando em conta letras maiusculas e minusculas
frase = ('Aprendendo String usando Python')
print(frase.replace('Python', 'java'))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# a função "in" confere se uma palavra esta dentro da frase

frase = ('Aprendendo String usando Python')
print('Aprendendo' in frase)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# a função "find" busca a posição de inicio de uma determinada palavra

frase = ('Aprendendo String usando Python')
print(frase.find('Python'))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# a função "split" cria uma lista semparando cada palavra

frase = ('Aprendendo String usando Python')
print(frase.split())

# referencia ==   https://youtu.be/a7DH88vk2Sk?t=1793   ==
