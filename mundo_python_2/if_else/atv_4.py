# escreva um progarma que ira pegurntar a idade de um jovem e ira calcular se ele e maior menor ou igual a 18
# e mostre se ele ira se alistar, se ele tem que se alistar, ou se ja passo do tempo de alistamento.

from datetime import date

data_atual = date.today()

idade = int(input("Em que ano voce nasceu? "))

resul = data_atual.year - idade

if resul < 18:
    print(f"voce tera que fazer o alistamento em {resul} anos")
elif resul == 18:
    print("esta na hora de voce fazer o seu alistamento")
else:
    print("o tempo de alistamento ja passo")

    confirm = input("\nvoce ja fez o alistamento militar? ")

    if confirm == "sim" or "s":
        print("muito obrigado")
    else:
        print("pague a multa em nosso site")