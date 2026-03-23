import re

# Defina a expressão regular que deseja testar
padrao = r"[A-Z][a-z]{1,39}"

# Defina a string que deseja testar
texto = "Leonardo"

# Tente encontrar uma correspondência da expressão regular na string
correspondencia = re.search(padrao, texto)

# Verifique se houve uma correspondência e imprima o resultado
if correspondencia:
    print("A string corresponde à expressão regular.")
else:
    print("A string não corresponde à expressão regular.")
