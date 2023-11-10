# leia dois valores depois mostre o menu: 1-soma  2-subtrai  3-maior  4-novos numero  5-encerrar
while True:

    numa = int(input("digite valor de a: "))
    numb = int(input("digite valor de b: "))

    decisao = int(input("1-soma  2-subtrai  3-maior  4-novos numero  5-encerrar: "))

    if decisao == 1:
        print("a soma dos numeros e: ", numa+numb)
    if decisao == 2:
        print("a subtração dos numeros e: ", numa-numb)
    
    if decisao == 3:
        if numa > numb:
            print("numero a e maior ")
        if numb > numa:
            print("numero b e maior")
        else:
            print("numeros iguais")
        
    if decisao == 4:
        continue
    
    if decisao == 5:
        break
        