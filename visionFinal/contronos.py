import numpy as np
import cv2

camara = cv2.VideoCapture(0) # Cargamos el vídeo

while (True):  
    (video, cuadro) = camara.read() #  leemos la camara
    if not video:# Si hemos llegado al final del vídeo salimos
        break
    imgg = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)# Convertimos a escala de grises
    imggs = cv2.GaussianBlur(imgg, (91, 91), 0)# Aplicamos suavizado para eliminar ruido
    imggsb = cv2.threshold(imggs, 120, 255, cv2.THRESH_BINARY)[1] #binariso a imgvg
    imgf = cv2.cvtColor(imggsb, cv2.COLOR_GRAY2BGR)# Convertimos a colores para agregar el contorno
    contor, hierarchy = cv2.findContours(imggsb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # detecta los cambios entre blacon y negrto y los combiente en contorno
    cv2.drawContours(imgf, contor,-1,(0,0,255),2) #dibuja contorno sobre la imagen imgf
    cv2.drawContours(cuadro, contor, -1, (0,0,255),2) # dibuja contorno sobre la imagen cuadro
    cv2.imshow("video contorno", imgf) 
    cv2.imshow("video imagen", cuadro)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
     
camara.release()  # Liberamos la cámara
cv2.destroyAllWindows() # cerramos todas las ventanas
 