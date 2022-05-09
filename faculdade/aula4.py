# pip install opencv-python
# pip install numpy

from cv2 import cv2
import numpy as np

img = cv2.imread(r'diretorio da imagem') # : 'mais diretorio'

cinza = cv2.cvtcolor(img, cv2.COLOR_GRAY) # CONVENTENDO IMAGEM PARA CINZA
