import cv2
import numpy as np

change = False                                      # Verdadero si el mouse es presionado
img = cv2.imread('/Users/Arcano/Desktop/lena.JPG')  # Leemos la imagen
fila, columna = img.shape[:2]  # Obtenemos sus dimensiones height alto width ancho
img1 = np.zeros((fila, columna, 3), np.uint8)  # Creamos una imagen de ceros
img2 = np.zeros((fila, columna, 3), np.uint8)  # Creamos una imagen de ceros


def draw(event, x, y, flags, param): # funcion de llamado del mouse
    global  change                   # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        change = True                   # En caso de ser verdado se asigna una variable boleana
        for i in range(x-2,x+2 ):
            for j in range(y-2, y+2):
                if np.all(img1[j,i])==np.all(img2[j,i]) :
                    b = img[j,i,0]
                    g = img[j,i,1]
                    r = img[j,i,2]
                    img[j,i,0] = r
                    img[j,i,1] = b
                    img[j,i,2] = g
                    img1[j,i] = [100,100,100]

    elif event == cv2.EVENT_MOUSEMOVE:  # Cuando se mueva el mouse
        if change == True:              # Si se verdadera la condicion de dibujo
           for i in range(x-2,x+2 ):
                for j in range(y-2, y+2):
                    if np.all(img1[j,i])==np.all(img2[j,i]) :
                        b = img[j,i,0]
                        g = img[j,i,1]
                        r = img[j,i,2]
                        img[j,i,0] = r
                        img[j,i,1] = b
                        img[j,i,2] = g
                        img1[j,i] = [100,100,100]


    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
        change = False                  # Que ya no dibuje
       

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)  # Muestro las imagenes

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
        break

cv2.destroyAllWindows()