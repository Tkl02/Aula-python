lista = []


def create_date():
    temp_list = []
    print("------------- Insert Informations -----------")
    name = input("name: ")
    last_name = input("last_name: ")
    age = input("age: ")
    number = input("Number: ")

    temp_list.extend([name, last_name, age, number])
    lista.append(temp_list)


def read_date():
    if lista.__len__() < 1:
        print("Error: This list is empty")
        return

    print("------------- read information -----------")
    list_len = len(lista)
    indice_one = int(input(f"Insert index to read complete data[0:{list_len-1}]: "))
    indice_two = input(
        "Insert: Name [0] | LastName [1] | Age [2] | Number [3] | All [None]:  "
    ).lower()
    if indice_one >= 0 and indice_one < len(lista):
        if indice_two in ["name", "0"]:
            print("------------------------")
            print(lista[indice_one][0])
            print("------------------------")

        elif indice_two in ["lastname", "1"]:
            print("------------------------")
            print(lista[indice_one][1])
            print("------------------------")

        elif indice_two in ["age", "2"]:
            print("------------------------")
            print(lista[indice_one][2])
            print("------------------------")

        elif indice_two in ["number", "3"]:
            print("------------------------")
            print(lista[indice_one][3])
            print("------------------------")

        else:
            print("Error: to print list [indice two] information")
    else:
        print("Error: to print list [indice one] information")


def update_date():
    if lista.__len__() < 1:
        print("Error: This list is empty")
        return

    print("------------- Update information -----------")
    indice_one = int(input(f"Insert index to update [0:{len(lista)-1}]: "))
    indice_two = input(
        "Insert: Name [0] | LastName [1] | Age [2] | Number [3]:  "
    ).lower()

    if indice_one >= 0 and indice_one < len(lista):
        if indice_two in ["name", "0"]:
            print("------------------------")
            name = input("name: ")
            lista[indice_one][0] = name
            print("-----Update success-----")

        elif indice_two in ["lastname", "1"]:
            print("------------------------")
            last_name = input("LastName: ")
            lista[indice_one][1] = last_name
            print("-----Update success-----")

        elif indice_two in ["age", "2"]:
            print("------------------------")
            age = input("age: ")
            lista[indice_one][2] = age
            print("-----Update success-----")

        elif indice_two in ["number", "3"]:
            print("------------------------")
            number = input("Number: ")
            lista[indice_one][3] = number
            print("-----Update success-----")

        else:
            print("Error: to print list [indice two] information")
    else:
        print("Error: to print list [indice one] information")


def delete_date():
    if lista.__len__() < 1:
        print("Error: This list is empty")
        return
    indice_to_delete = int(input(f"Insert index to delete [0:{len(lista)-1}]: "))

    if indice_to_delete >= 0 and indice_to_delete < len(lista):
        confirm = input("Are you sure? (Y/N): ")
        if confirm.lower() in ["n", "no"]:
            print("Delete canceled")
        elif confirm.lower() in ["y", "ye", "yes"]:
            del lista[indice_to_delete]
            print("-----Delete success-----")
    else:
        print("Error: invalid index")


if __name__ == "__main__":

    option = ""

    while option.lower() not in ["exit", "quit", "q"]:

        print("\n__________________CRUD database__________________")
        print("CREATE [0] | READ [1] | UPDATE [2] | DELETE [3] | EXIT [Q]")
        print("-------------------------------------------------")
        option = input("Choose an option: ")

        if option.lower() in ["create", "0"]:
            create_date()

        elif option.lower() in ["read", "1"]:
            read_date()

        elif option.lower() in ["update", "2"]:
            update_date()

        elif option.lower() in ["delete", "3"]:
            delete_date()

        elif option.lower() in ["exit", "quit", "q"]:
            break

        else:
            print("Invalid option! Please try again.")

    print("\n____________Good Bye____________")
