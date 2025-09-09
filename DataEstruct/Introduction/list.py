# Create List
fruits = ['maça', 'banana', 'mamão', 'laranja', 'abacaxi', 'abacata']
print(f"Lista de Fruitas {fruits}")

# access with indice ( O(1) )
first_fruit = fruits[5]
print(f"Ultima fruta {first_fruit}")


# finaly add ( O(1) )
fruits.append('uva')
print(f"Lista de frutas depois do append {fruits}")

# insert at the beginning
# o inserte força com que todo os itens da minha lista sejam movidos uma casa para frente para adicionar o valor no inicio, fazendo com que ele seja ( O(n) )
fruits.insert(0, 'jabuticaba')
print(f"Lista de fruitas depois da adição {fruits}")
# remove at the beginning
# remove o indice do inicio fonçando todos os outros indices a voltarem uma casa, fazendo com que ele seja ( O(n) )
fruit_remove = fruits.pop(0)
print(f"Lista de Fruitas depois da remoção {fruit_remove}")


# Busca ( O(n) )
if "banana" in fruits:
    print("tem banana")