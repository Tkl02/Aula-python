def calcular_digito(cpf_slice: str, peso_inicial: int) -> int:
    soma = 0
    peso = peso_inicial

    for digit in cpf_slice:
        soma += int(digit) * peso
        peso -= 1

    resto = (soma * 10) % 11
    return resto if resto < 10 else 0


def validar_cpf(cpf: str) -> bool:
    cpf = "".join([c for c in cpf if c.isdigit()])

    if len(cpf) != 11:
        return False
        
    # (opcional) apenas para tratamento de erros.
    # if not cpf.isdigit():
    #     return False

    if cpf == cpf[0] * 11:
        return False

    d1 = calcular_digito(cpf[:9], 10)
    d2 = calcular_digito(cpf[:10], 11)

    return d1 == int(cpf[9]) and d2 == int(cpf[10])


if __name__ == "__main__":
    cpf = input("Informe o CPF: ")

    if validar_cpf(cpf):
        print(f"CPF ({cpf}) é válido")
    else:
        print("CPF inválido")
