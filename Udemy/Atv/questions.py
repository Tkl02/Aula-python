questions = [
    {"question": "quanto é 2³?", "options": [2, 4, 6, 8], "resposta": 3},
    {"question": "quanto é raiz de 144?", "options": [14, 12, 6, 16], "resposta": 1},
    {
        "question": "quanto é 124/22?",
        "options": [5.63, 56.3, 12.3, 22.4],
        "resposta": 0,
    },
]


def question_resolution():
    acertos = 0  # Inicializar a variável
    for questoes in questions:
        print(questoes.get("question"))
        print()

        for indice, opcoes in enumerate(questoes.get("options")):
            print(f"{indice}) {opcoes}")

        escolha = int(input("escolha uma opção: "))

        if escolha == questoes["resposta"]:  # Comparar índices
            print("👍")
            acertos += 1
        else:
            print("❌")

        print(escolha)
        print(questoes["resposta"])

    print(f"Total de acertos: {acertos}/{len(questions)}")


if __name__ == "__main__":
    question_resolution()
    print("_____ END GAME _____")
