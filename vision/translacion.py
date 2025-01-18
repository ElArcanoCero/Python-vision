import numpy as np
import cv2

img1 = cv2.imread('gamma.jpg')  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
print(img1.shape)
img2 = np.zeros((height*2, width*2, 3), np.uint8)  # Creamos una imagen nueva
transMat = np.array([[1, 0, 250], [0, 1, 50]])  # Creamos la matriz de transformacion

for i in range(0, height):
    for j in range(0, width):
        pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
        translation = np.dot(transMat, pos)  # Realizamos el producto punto entre las martices
        #print(translation[1])
        img2[translation[0], translation[1]] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('resultado1', img1)
cv2.imshow('resultado2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
