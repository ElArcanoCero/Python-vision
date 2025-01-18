import numpy as np
import cv2

img1 = cv2.imread('/Users/Arcano/Desktop/img1.png', 0) # Leemos la imagene
img2= cv2.imread('/Users/Arcano/Desktop/img2.png')
img3= cv2.imread('/Users/Arcano/Desktop/img3.png')  


img1Fg = cv2.GaussianBlur(img1, (5, 5), sigmaX=-1, sigmaY=-1)  # filtro gaus
cv2.imshow('ruido gausiano', img1)
cv2.imshow('imagen con filtro gausiano', img1Fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2Fm = cv2.medianBlur(img2, 3)
img2k=np.array([[1, 2, 1], [2, 4, 2],[1, 2, 1]])/16 # kernel para piso paso bajo               
#img2k = np.ones((5, 5), np.uint8)/25
img2Fb= cv2.filter2D(img2Fm, ddepth=-1, kernel=img2k, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D 
cv2.imshow('riudo aditivo', img2)
cv2.imshow('imagen con filtro paso bajo', img2Fb)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3Fm = cv2.medianBlur(img3, 3)
img3Fb= cv2.filter2D(img3Fm, ddepth=-1, kernel=img2k, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D 
cv2.imshow('ruido sal y pimienta', img3)
cv2.imshow('imagen con filtro mediana', img3Fb)
cv2.waitKey(0)
cv2.destroyAllWindows()