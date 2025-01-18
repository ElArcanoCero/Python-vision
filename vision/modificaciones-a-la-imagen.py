from pickletools import anyobject
import numpy as np
import cv2
import math

img1 = cv2.imread('C:/Users/Arcano/OneDrive/Escritorio/pyton/visionFinal/logo.png')  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones height alto width ancho
x = math.pow(height,2)
y = math.pow(width,2)
z = math.sqrt(x+y) # calculamos la diagonal
z = int(z) # convertimos la diagonal a un entero
print (height)
img2 = np.zeros((z, z, 3), np.uint8)  # Creamos una imagen de ceros
img3 = np.zeros((z, z, 3), np.uint8)  # Creamos una imagen de ceros
img4 = np.zeros((z, z, 3), np.uint8)  # Creamos una imagen de ceros
img5 = np.zeros((z*2, z*2, 3), np.uint8)  # Creamos una imagen de ceros
img6 = np.zeros((z*2, z*2, 3), np.uint8)  # Creamos una imagen de ceros
img7 = np.zeros((z*2, z*2, 3), np.uint8)  # Creamos una imagen de ceros
img8 = np.zeros((z*3, z*3, 3), np.uint8)  # Creamos una imagen de ceros
img9 = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen de ceros
img10 = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen de ceros

for i in range(0, height):
    for j in range(0, width):
        xr = round((i*(math.cos(np.pi/4)))-(j*(math.sin(np.pi/4)))) #posicion para i
        yr = (round(((i*(math.sin(np.pi/4)))+(j*(math.cos(np.pi/4))))))   #posicion para j
        if xr >= 0:
            xr = round( xr - (z/2))
            img2[(((int(xr)))), ((int(yr)))] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
            
        else:
            xr = round(xr + (z/2))
            img2[(((int(xr)))), ((int(yr)))] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
           
            
for i in range(0, z-1):
    for j in range(0, z-1):
        if np.all(img2[i,j])==np.all(img3[i,j]) :
            img3[i,j] = (img2[i,j+1]/[2,2,2])+(img2[i+1,j]/[2,2,2]) #tabulado 
            img2[i,j] = img3[i,j] # llenado de informacion faltante
        
cv2.imshow('resultado', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, z):
    n=0
    for j in range(0, z):
        xr = round((i-(j*(math.tan(0.17))))) #posicion para i
        yr = round(j)                        #posicion para j
        
        if xr >= 0:
            xr = xr - height
            img4[(((int(xr)))), ((int(yr)))] = img2[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
            
        else:
            xr =  xr + 27
            img4[(((int(xr)))), ((int(yr)))] = img2[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
            
cv2.imshow('resultado2', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, z):
    for j in range(0, z):
        
        xr = round (i + 50) #posicion para i
        yr = round (j + 50) #posicion para j
        img5[(((int(xr)))), ((int(yr)))] = img4[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
       
cv2.imshow('resultado3', img5)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, z*2):
    for j in range(0, z*2):
        
        xr = round (i - 50) #posicion para i
        yr = round (j - 50) #posicion para j
        img6[(((int(xr)))), ((int(yr)))] = img5[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
       
cv2.imshow('resultado4', img6)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, z):
    for j in range(0, z):
        xr = round((i+(j*(math.tan(0.17))))) #posicion para i
        yr = round(j)                        #posicion para j
        img7[(((int(xr)))), ((int(yr)))] = img6[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('resultado5', img7)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0, (z*2)-1):
    for j in range(0, (z*2)-1):
        xr = round((i*(math.cos(np.pi*7/4)))-(j*(math.sin(np.pi*7/4)))) #posicion para i
        yr = round(((i*(math.sin(np.pi*7/4)))+(j*(math.cos(np.pi*7/4))))) #posicion para j
        #img8[(((int(xr)))), ((int(yr)))] = img7[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
        
        xr = xr - 147
        yr = yr + 132
        img8[(((int(xr)))), ((int(yr)))] = img7[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen
            
        
for i in range(0, height):
    for j in range(0, width):
        
        img10[i,j] = img8[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

for i in range(0, height-1):
    for j in range(0, width-1):
        if np.all(img8[i,j])==np.all(img9[i,j]) :
            img9[i,j] = (img10[i,j+1]/[2,2,2])+(img10[i+1,j]/[2,2,2]) #tabulado 
            img10[i,j] = img9[i,j] # llenado de informacion faltante 
            
cv2.imshow('resultado6', img10)
cv2.imshow('resultado7', img1)
cv2.imshow('resultado8', img8)
cv2.waitKey(0)
cv2.destroyAllWindows()