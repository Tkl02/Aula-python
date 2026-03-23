#crie um programa que leia as notas do aluno e mostre se ele atingiu a media final
# falando se ele foi aprovado reprovado ou esta de recuperaçao

nota1 = float(input("qual a primeira nota? "))
nota2 = float(input("qual a segunda nota? "))

media = (nota1 + nota2)/2

if media < 50:
    print("\033[31m aluno reprovado \033[m")

elif media >=50 and media < 70:
    print("\033[33m aluno de recuperaçao\033[m")

else:
    print("\033[32m aluno aprovado \033[m")