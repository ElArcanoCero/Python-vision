import cv2
import numpy as np


img = cv2.imread('/Users/Arcano/Desktop/lena.JPG')  # Leemos la imagen
drawing = False  # Verdadero si el mouse es presionado
ix, iy = -1, -1

#  funcion de llamado del mouse
def draw(event, x, y, flags, param): # Se declara la funcion
    global ix, iy, drawing, mode  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        ix, iy = x, y  # Almacenamos la poscion incial en las variales

    
    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
        drawing = False  # Que ya no dibuje
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness=1)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw)  # Muestro las imagenes
        fila = x-ix
        columna = y - iy
        img1 = np.zeros((columna*2, fila*2, 3), np.uint8)  # Creamos una imagen de ceros
        for i in range(ix, x-1):
            for j in range(iy, y-1):
                for k in range(0, 2):
                     for j in range(0, 2):
                        img1[j-iy,i-ix] = img[j,i]
        cv2.imshow('resultado', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)  # Muestro las imagenes

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(ix, iy)
        # Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
        break

cv2.destroyAllWindows()
