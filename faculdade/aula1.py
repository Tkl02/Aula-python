nome_aluno = ["alexandre","lucas","leo","joao","zeze","felipe"]

with open ("aluno.txt", "w") as writer:
    for aluno in nome_aluno:
    writer.write(aluno+"\n")