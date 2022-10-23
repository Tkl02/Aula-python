# escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. O programa dever perguntar:
# o valor da casa, o seu salario e em quantos anos vc deseja pagar. calcule a pretaçao mensal, sabendo que ela
# não pode exerder 30% do valor do salario. caso contrario o emprestimo sera negado

casa =  float(input("qual o valor da casa ? "))
salario = float(input("qual o seu salario ? "))
anos = int(input("dividir em quantos anos ? "))

prestaçao =  salario * 0.3
parcela = casa / anos

if parcela > prestaçao:
    print("-= \033[31m compra negada \033[m =-")
if parcela < prestaçao:
    print("-= \033[32m compra aprovada \033[m =-")
    print("parcelas de {:.2f} por mes.".format(parcela))

