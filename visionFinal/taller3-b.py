import numpy as np
import cv2
import time

camara = cv2.VideoCapture(0) # Cargamos el vídeo

ban = 0;
tam = 90

while (True):  
    (video, cuadro) = camara.read() #  leemos la camara
    if not video:# Si hemos llegado al final del vídeo salimos
        break
    hei, wid = cuadro .shape[:2]  # Obtenemos sus dimensiones
    img1 = np.zeros((180, 180), np.uint8)
    imgr = cuadro[hei//2-tam:hei//2+tam, wid//2-tam:wid//2+tam]  # recorta un recuadro en el cenmtro de la imagen
    img1 = cv2.cvtColor(imgr, cv2.COLOR_BGR2GRAY)  # Conversion a escala de grises
    imgg = cv2.GaussianBlur(img1, (9, 9), 0)# Aplicamos suavizado para eliminar ruido
    imgc = cv2.Canny(imgg, 60, 200) #filtro canny
    kern1 = np.ones((3,3), np.uint8)   # creo un kernel para dilatar
    imgd= cv2.dilate(imgc, kern1, iterations=1) # dilatar 
   
    cuadro[hei//2:hei//2+1, 0 : (wid//2)-tam] = [0,0,255]
    cuadro[hei//2:hei//2+1, (wid//2)+tam+1 : wid] = [0,0,255]
    cuadro[0 : (hei//2)-tam+15,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[(hei//2)+tam-14 : hei ,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[(hei//2)-5 : (hei//2)+6 ,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[hei//2:hei//2+1, (wid//2)-5 : (wid//2)+6] = [0,0,255]
    cv2.rectangle(cuadro, (wid//2-tam,hei//2-tam+15), (wid//2+tam+1,hei//2+tam-14), (0,0,255)) # enmarco la zona donde se realizara la lectura
    
    cv2.putText(cuadro, 'centra el codigo', ((wid//2)-tam-50, (hei//2)-tam-10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
   
            
    cv2.imshow("video 1", cuadro)
    #cv2.imshow("video 2", imgs)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    
camara.release()  # Liberamos la cámara 
cv2.destroyAllWindows() #cerramos todas las ventanas