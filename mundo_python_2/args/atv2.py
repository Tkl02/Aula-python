def exponenciacao(numero, expoente):

    if expoente == 0:
        resultado = 1
        return resultado
    if expoente <= 0:
        resultado = "Erro: expoente negativo"
        return resultado

    for _ in range(expoente-1):
        numero += numero
    
    return numero



if __name__ == "__main__":
    numero =2
    expoente =-1

    resultado = exponenciacao(numero, expoente)
    print(resultado)