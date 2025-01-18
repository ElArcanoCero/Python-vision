# Punto B

# Se importan las librerías
import numpy as np
import cv2
from matplotlib import pyplot as plt

#Procedimiento. Imagen 1
img1 = cv2.imread('Campo_oscuro.jpg', 0)  # Leemos la imagen en escala de grises
img_1 = cv2.resize(img1, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC) #redimensionamos la imagen
cv2.imshow('Campo_oscuro', img_1) #Muestra la imagen original en la escala de grises. 
cv2.waitKey(0)
t, img_oscuro = cv2.threshold (img_1, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_TRIANGLE) # Umbralizacion con operador binario y THRESH_TRIANGLE: Calcula el umbral optimo de manera automatica
contours, hierarchy = cv2.findContours(img_oscuro, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Obtenemos los contornos
cv2.imshow('Imagen umbralizada campo oscuro', img_oscuro) # Se aplica filtro y luego se umbraliza la imagen
cv2.waitKey(0)

#Procedimiento. Imagen 2
img2 = cv2.imread('Frontal.jpg', 0)  # Leemos la imagen en escala de grises
img_2 = cv2.resize(img2, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC) #redimensionamos la imagen
height, width = img_2.shape 
cv2.imshow('Frontal', img_2) #Muestra la imagen original en la escala de grises. 
cv2.waitKey(0)
t1, img_frontal = cv2.threshold (img_2, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_TRIANGLE) # Umbralizacion con operador binario y THRESH_TRIANGLE: Calcula el umbral optimo de manera automatica
contours, hierarchy = cv2.findContours(img_frontal, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Obtenemos los contornos
cv2.imshow('Imagen umbralizada frontal', img_frontal) # Se aplica filtro y luego se umbraliza la imagen
cv2.waitKey(0)

#Procedimiento. Imagen 3
img3 = cv2.imread('Lateral.jpg', 0)  # Leemos la imagen en escala de grises
img_3 = cv2.resize(img3, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC) #redimensionamos la imagen
cv2.imshow('Lateral', img_3) #Muestra la imagen original en la escala de grises. 
cv2.waitKey(0)
t2, img_lateral = cv2.threshold (img_3, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_TRIANGLE) # Umbralizacion con operador binario y THRESH_TRIANGLE: Calcula el umbral optimo de manera automatica
contours, hierarchy = cv2.findContours(img_lateral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Obtenemos los contornos
cv2.imshow('Imagen umbralizada lateral', img_lateral) # Se aplica filtro y luego se umbraliza la imagen
cv2.waitKey(0)

#Para conocer el ancho de cada barra y el número de barras utilizamos la imagen 2. 
n=0;contador=0;tam={}

#Se hace un ciclo for para identificar el tamaño del ancho y el alto
for j in range(0, width): #Se evalua el ancho de la imagen 	
    #Se evalua los altos de la imagen
	if img_frontal[height//2, j] == 255:
		if contador>0:
		   tam[n]=contador
		   contador=0
		   n=n+1	
	if img_frontal[height//2, j] == 0:
		contador=contador+1
	img_frontal[height//2, j]
cantidad_barras=len(tam)

print('Número de barras:',cantidad_barras)
print('Tamaño de las baras en pixeles:',tam)
