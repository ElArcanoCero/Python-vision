import cv2
import numpy as np

drawing = False  # Verdadero si el mouse es presionado
ix, iy = -1, -1

def zoom(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)

#  funcion de llamado del mouse
def draw(event, x, y, flags, param): # Se declara la funcion
    global ix, iy, drawing, mode  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        ix, iy = x, y  # Almacenamos la poscion incial en las variales

    elif event == cv2.EVENT_MOUSEMOVE:  # Cuando se mueva el moue
        if drawing == True:  # Si se verdadera la condicion de dibujo
            imgNew = cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness=1)  # Comando para dibujar un rectangulo
               
                
            cropped = imgNew[200:300, 150:250]
            zoomed2 = zoom(imgNew, 2)
            zoomed4 = zoom(imgNew, 4)
            zoomed6 = zoom(imgNew, 6)
            zoomed_and_cropped = zoom(cropped, 3)
               
            cv2.imshow("nueva imagen zoom por 2",zoomed2)
            cv2.imshow("nueva imagen zoom por 4",zoomed4)
            cv2.imshow("nueva imagen zoom por 6",zoomed6)

    elif event == cv2.EVENT_LBUTTONUP:  # Cuando se levante el boton
        drawing = False  # Que ya no dibuje
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

# path 
path = r'C:\Users\Sebastian\Downloads\lena.jpg'
# Reading an image in default mode
img = cv2.imread(path)
# img = np.zeros((500, 500, 3), np.uint8)  # Creo una imagen vacia
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)  # Muestro las imagenes

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(ix, iy)
        # Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
        break

cv2.destroyAllWindows()

# Fuente: Documentación OpenCV 