import sys
import os

def help_menu():
    print("""
-h or --help -> mostra o menu de ajuda
-l or --lines -> mostra o número total de linhas
-w or --words -> mostra o número total de palavras
-c or --chars -> mostra o número total de caracteres
-a or --all -> executa todas as análises acima
          
python analisador.py texto.txt --linhas

    """)
def search_word(content, word):
    words = content.split()
    
    for w in words:
        if w == word:
            return f"Palavra '{word}' presente no texto"
    
    return f"Palavra '{word}' não encontrada"


def lines_counter(content):
    return len(content.splitlines())

def words_counter(content):
    return len(content.split())

def chars_counter(content):
    return len(content)

def read_archive(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Erro: numero de argumentos insuficiente", help_menu())
        return 
    
    # if len(sys.argv) > 3:
    #     return "Erro: numer do argumentos exedidos", help_menu()
    
    file_path = sys.argv[1]
    args = sys.argv[2:]

    if not os.path.exists(file_path):
        print("Erro: arquivo não encontrado")
        return


    if "-h" in args or "--help" in args:
        return help_menu()

    content = read_archive(file_path)

    if "-a" in args or "--all" in args:
        print ("linhas: ", lines_counter(content))
        print("Palavras: ", words_counter(content))
        print("caracteres: ",chars_counter(content))
        return


    i = 0
    while i < len(args):
        arg = args[i]

        if arg in ("-l", "--lines"):
            print("Linhas:", lines_counter(content))

        elif arg in ("-w", "--words"):
            print("Palavras:", words_counter(content))

        elif arg in ("-c", "--chars"):
            print("Caracteres:", chars_counter(content))

        elif arg in ("-s", "--search"):
            if i + 1 >= len(args):
                print("Erro: palavra de busca não informada")
                return
            print(search_word(content, args[i + 1]))
            i += 1

        i += 1

if __name__ == "__main__":
    main()