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
    cuadro[0 : (hei//2)-tam,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[(hei//2)+tam+1 : hei ,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[(hei//2)-5 : (hei//2)+6 ,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[hei//2:hei//2+1, (wid//2)-5 : (wid//2)+6] = [0,0,255]
    cv2.rectangle(cuadro, (wid//2-tam,hei//2-tam), (wid//2+tam+1,hei//2+tam+1), (0,0,255)) # enmarco la zona donde se realizara la lectura
    
    cv2.putText(cuadro, 'centra la imagen', ((wid//2)-tam-50, (hei//2)-tam-10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
   
    #cv2.floodFill(imgd,None, (tam,tam),255, 0, 100)  # rellono el contorno si esta en el centro de la imagen
    imgd = np.invert(imgd)
    npx = np.size(imgd)
    kern2 = np.zeros(imgd.shape, np.uint8)
    
    _,imgd = cv2.threshold(imgd,120,255,0) # paso a binaria
    kern3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    
    
    for i in range(60):
    #Step 2: Open the image
        open = cv2.morphologyEx(imgd, cv2.MORPH_OPEN, kern3)
        #Step 3: Substract open from the original image
        temp = cv2.subtract(imgd, open)
        #Step 4: Erode the original image and refine the skeleton
        eroded = cv2.erode(imgd, kern3)
        kern2 = cv2.bitwise_or(kern2,temp)
        imgd = eroded.copy()

    imgs=kern2
    
    kern1 = np.ones((3,3), np.uint8)   # creo un kernel para dilatar
    imgs= cv2.dilate(kern2, kern1, iterations=1) # dilatar 
    
    maskC = np.zeros((180,180),np.uint8) # creo una imagen de ceros
    
    
    cv2.circle(maskC, (90,90), 30, 255, 3) # pongo un circulo blanco en la imagen de ceros
    cue = np.count_nonzero(cv2.bitwise_and(imgs, maskC)) #cuentos cuantas linesas se crusan
    print (cue)
    if cue >= 50 and cue <= 65:
        cv2.putText(cuadro, 'triangulo', ((wid//2)-70, (hei//2)+60), cv2.FONT_HERSHEY_PLAIN, 2, (0,255, 0), 2)
        pts = np.array([[10,5],[20,30],[70,20]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(imgs,[pts],True,(0,255,255))
    
    
       
    cv2.circle(imgs, (90,90), 30, 255, 3)          
    cv2.imshow("video 1", cuadro)
    cv2.imshow("video 2", imgs)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    
camara.release()  # Liberamos la cámara 
cv2.destroyAllWindows() #cerramos todas las ventanas
