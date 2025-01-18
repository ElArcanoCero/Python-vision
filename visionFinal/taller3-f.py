import numpy as np
import cv2



img = cv2.imread('/Users/Arcano/Downloads/img5.png') # Leemos la imagene
height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgg = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, imgg)
ret, imginv = cv2.threshold(imgg, 128, 255, cv2.THRESH_BINARY_INV)#invertir blancos y negros
kern1 = cv2.getStructuringElement(cv2.MORPH_CROSS, ksize=(3, 3), anchor=(-1, -1))
imgd = cv2.dilate(imginv , kern1, iterations=1)
ret, imginv = cv2.threshold(imgd, 128, 255, cv2.THRESH_BINARY_INV)#invertir blancos y negros
imgg = cv2.GaussianBlur(imginv, (3, 3), 0)# Aplicamos suavizado para eliminar ruido
cv2.imshow("original2", img)
#cv2.imshow('salida 1', ) 
cv2.imshow('salida 2', imgg) 
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('/Users/Arcano/Downloads/img6.png') # Leemos la imagene

height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgg = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, imgg)
ret, imginv = cv2.threshold(imgg, 128, 255, cv2.THRESH_BINARY_INV)#invertir blancos y negros
kern1 = cv2.getStructuringElement(cv2.MORPH_CROSS, ksize=(3, 3), anchor=(-1, -1))
for i in range(1, 4):
    ret, imginv = cv2.threshold(imgg, 128, 255, cv2.THRESH_BINARY_INV)#invertir blancos y negros
    imgd = cv2.dilate(imginv , kern1, iterations=1)
    ret, imginv = cv2.threshold(imgd, 128, 255, cv2.THRESH_BINARY_INV)#invertir blancos y negros
    imgg = cv2.GaussianBlur(imginv, (3, 3), 0)# Aplicamos suavizado para eliminar ruido
    imgo = cv2.erode(imginv, kern1, iterations=1)
    
imgo = cv2.dilate(imgo , kern1, iterations=4)
imgg = cv2.GaussianBlur(imgo, (3, 3), 0)# Aplicamos suavizado para eliminar ruido

cv2.imshow("original2", img)
cv2.imshow('salida 1', imgo ) 
cv2.imshow('salida 2', imgg) 
cv2.waitKey(0)
cv2.destroyAllWindows()