#criando coodigo de barras

from barcode import EAN13 # importa funçao da biblioteca barcode(gerador de codigo de barra em varios formatos)
from barcode.writer import ImageWriter # importa funçao da biblioteca barcode(gerador de codigo de barra em varios formatos)

with open (r'C:\Users\second\Pictures\Camera Roll\test.png', 'wb') as f:
# ele abre um aquivo se o arquivo nao exister ele ira gerar um.
# W(aberto para escrita, truncando o arquivo primeiro) b(modo binário)= WB
# as f (definiçao de "expressões ") 

EAN13(str(123456789854), writer = ImageWriter()).write(f)

# EAN13(tipo de codigo a ser gerado)
# str (atribuindo numeros de 12 char para ser lido)
# imagewriter gerando codigo de barras com os numeros lido pela str ja convertido com a "expressões" f
