#criando coodigo de barras

from barcode import EAN13
from barcode.writer import ImageWriter

with open (r'C:\Users\second\Pictures\Camera Roll\test.png', 'wb') as f:
    EAN13(str(123456789854), writer = ImageWriter()).write(f)
