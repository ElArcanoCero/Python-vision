from pickletools import anyobject
from tracemalloc import stop
import numpy as np
import cv2



img1 = cv2.imread('C:/Users/Arcano/OneDrive/Escritorio/pyton/visionFinal/logo.png')  # Leemos la imagen
filas, columnas, fondo = img1.shape  # Obtenemos sus dimensiones height alto width ancho
img6 = np.zeros((columnas, filas, 3), np.uint8)  # Creamos una imagen de ceros

cv2.imshow('imagen', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

 
mat = cv2.getRotationMatrix2D(((filas/2) ,(columnas/2)), 90, 1.0) 
img2 = cv2.warpAffine(img1, mat, (filas, columnas))
cv2.imshow('resultado', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

mat1 = np.array([[1,-0.1,0],[0,1,0]])
mat1 = np.float32(mat1)
img3 = cv2.warpAffine(img2, mat1, (filas, columnas))
cv2.imshow('resultado2', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

mat2 = np.float32([[1,0,50],[0,1,50]])
mat2 = np.float32(mat2)
img4 = cv2.warpAffine(img3, mat2, (filas*2,columnas*2)) 
cv2.imshow('resultado3', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

mat3 = np.float32([[1,0,-50],[0,1,-50]])
mat3 = np.float32(mat3)
img5 = cv2.warpAffine(img4, mat3, (filas,columnas))
cv2.imshow('resultado4', img5)
cv2.waitKey(0)
cv2.destroyAllWindows()

                                     
pun1 = np.float32([[0,0],[filas ,0],[0,columnas],[filas-23,columnas]])
pun2 = np.float32([[0,0],[filas ,0],[0,columnas],[filas,columnas]])
mat4 = cv2.getPerspectiveTransform(pun1,pun2) 
img7 = cv2.warpPerspective(img5, mat4, (filas, columnas))
cv2.imshow('resultado5', img7)
cv2.waitKey(0)
cv2.destroyAllWindows()

mat5 = cv2.getRotationMatrix2D((filas-113,columnas-113), -90, 1.0) 
img8 = cv2.warpAffine(img7, mat5, (filas, columnas)) 
cv2.imshow('resultado6', img8)
cv2.waitKey(0)
cv2.destroyAllWindows()