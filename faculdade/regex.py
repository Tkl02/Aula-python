import re

verifica = True
padrao = '[A-Z][a-z]{1,39}'

while verifica == True:
        if verifica == True:
                name = str(input("qual o nome ? (min.2 max.40)"))
                name_reg = re.search(padrao,name)
                print("nome aceito")
                if verifica == True:
                        cpf = int(input("qual o cpf ? (model: xxx.xxx.xxx-xx)"))
                        cpf_reg = re.search(r'\d{3}.\d{3}.\d{3}-\d{2}',cpf)
                        print("cpf aceito")
                        if verifica == False:
                                password = str(input("qual a senha ? (começa numero termina letra min.4 max.10)"))
                                password_reg = re.search(r'[0-9]{1}[\w]{2,8}[a-zA-Z]{1}',password)
                                print("aceita")
                                if verifica == True:
                                        cell = int(input("qual o celular ? (model: +xxx(xx)xxxxx-xxxx)"))
                                        cell_reg = re.search(r'\+\d{3}\(\d{2}\)9\d{4}-\d{4}',cell)
                                else:
                                        break
                        else:
                                break
                else:
                        break
        else:
                print("nao aceita")



