import cv2
import numpy as np


imga = cv2.imread('/Users/Arcano/Desktop/22.jpg',0)  # Leemos la imagen
fil1, colum1 = imga.shape[:2]  # Obtenemos sus dimensiones filas columnas

imgFa=(np.zeros((fil1, colum1), np.uint8))
imgFb=(np.zeros((fil1, colum1), np.uint8))
imgk1=np.array([[-3, -1, -1, -1, -3], 
               [-1, 2, 2, 2, -1],
               [-1, 2, 8, 2, -1],
               [-1, 2, 2, 2, -1]
               ,[-3, -1, -1, -1, -3]])  # filtro paso alto
imgk2=np.array([[1, 1, 1, 1, 1], 
               [1, 2, 2, 2, 1],
               [1, 2, 8, 2, 1],
               [1, 2, 2, 2, 1]
               ,[1, 1, 1, 1, 1]])/40  # filtro paso bajo
imgFa = cv2.filter2D(imga, ddepth=-1, kernel=imgk1, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
imgFb= cv2.filter2D(imga, ddepth=-1, kernel=imgk2, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('original', imga)
cv2.imshow('filtro paso alto', imgFa)
cv2.imshow('filtro paso bajo', imgFb)
cv2.waitKey(0)
cv2.destroyAllWindows()
