"""
Faça um jogo de adivinhação de palavra chave.
o usuario podera digitar letras para tentar descobri a palavra chave.
casa a letra estaja na palavra chave a string sera revelada.
caso a letra ainda não foi encontrada mostrara um "*".
"""

import random
import os

# Diretório onde está o arquivo .py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDS_PATH = os.path.join(BASE_DIR, "words.txt")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    content = f.read()
    words = [word.strip() for word in content.split(",") if word.strip()]


key_word = random.choice(words)
char_in_word = ""
tentativas = 0

print(key_word)

print("_______ Game Star _______")

while True:
    char = input("Digite uma letra: ")

    if char == "0":
        break

    if len(char) != 1:
        tentativas += 1
        print("Digite apenas 1 letras")
        continue

    if char in key_word:
        char_in_word += char

    word_form = ""

    for secret_char in key_word:
        if secret_char in char_in_word:
            word_form += secret_char
        else:
            word_form += "*"
    tentativas += 1
    print(word_form)

    if "*" not in word_form:
        print(f"_______ Congratulation ({tentativas}x) _______")
        print("_______ Game End _______")
        break
