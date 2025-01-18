import numpy as np
import cv2
import time

img1 = cv2.imread('/Users/Arcano/Desktop/21_.JPG')  # Leemos la imagen
height, width = img1.shape[:2]    # Obtenemos sus dimensiones
print(img1.shape)
img2 = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen nueva

ban1 = 0
ban2 = 0
ban3 = 0
# Imagen ciclica
start_time = time.time()

# Seccion a color
for i in range(0, height):
    for j in range(0, width):
        if ban1 == 3:
            img2[i, j, 2] = img1[i, j, 2]
            ban1 = 0
            ban2 = 1
        if ban1 == 2:
            img2[i, j, 1] = img1[i, j, 1]
            ban1 = 3
        if ban1 == 1:
            img2[i, j, 0] = img1[i, j, 0]
            ban1 = 2
        if ban1 == 0 and ban2 == 0: 
            img2[i, j] = img1[i, j]
            ban1 = 1
        ban2 = 0
    ban3 = ban3+1   
    if ban3 == 4:
        ban3 = 0
    ban1 = ban3      

print('Tiempo de ejecucion de ciclos:', end="")
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('imagen ciclica', np.hstack([img2]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas