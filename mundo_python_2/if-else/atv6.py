from datetime import date

ano = int(input("Em que ano voce nasceu? "))

data = date.today()

idade = data.year - ano

if idade <= 9:
    print("voce esta na classe \033[3m mirim \033[m")
elif idade > 9 and idade <= 14:
    print("voce esta na classe \033[3m infanil \033[m")
elif idade > 14 and idade <=19:
    print("voce esta na classe \033[3m junior \033[m")
elif idade >19 and idade <= 20:
    print("voce esta na classe \033[3m senior \033[m")
else:
    print("voce esta na classe \033[3m master \033[m")


