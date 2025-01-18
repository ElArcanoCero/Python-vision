from pickletools import anyobject
import numpy as np
import cv2
import math

img1 = cv2.imread('/Users/Arcano/Desktop/21_.JPG')  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
x = math.pow(height,2)
y = math.pow(width,2)
z = math.sqrt(x+y) # calculamos la diagonal
z = int(z) # convertimos la diagonal a un estero
img2 = np.zeros((z, z, 3), np.uint8)  # Creamos una imagen de ceros
img3 = np.zeros((z, z, 3), np.uint8)  # Creamos una imagen de ceros

a = int(height/1.35)
b = int(width/40)
for i in range(0, height):
    for j in range(0, width):
        xr = round((i*(math.cos(np.pi/4)))-(j*(math.sin(np.pi/4)))) #posicion para i
        yr = round((i*(math.sin(np.pi/4)))+(j*(math.cos(np.pi/4)))) #posicion para j
        img2[(((int(xr))-a)), ((int(yr)))+b] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
       
for i in range(0, z-1):
    for j in range(0, z-1):
        if np.all(img2[i,j])==np.all(img3[i,j]) :
            c = img2[i,j+1]+img2[i+1,j]
            d = [2,2,2]
            f = [0,0,0]
            f = c/d
            f = f.astype(np.int64)
            img2[i,j] = f.astype(np.int)
            #print(img2[i,j])
        
cv2.imshow('resultado', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


