import numpy as np
import cv2

camara = cv2.VideoCapture(0) # Cargamos el vídeo

# HSV
red1h = np.array([177, 120, 110],np.uint8)
red2h = np.array([179, 230, 255], np.uint8)
gre1h = np.array([65, 100, 60],np.uint8)
gre2h = np.array([75, 130, 160], np.uint8)
blu1h = np.array([110, 140, 100],np.uint8)
blu2h = np.array([115, 205, 210], np.uint8)
ora1h = np.array([0, 150, 140],np.uint8)
ora2h = np.array([4, 255, 250], np.uint8)
yel1h = np.array([24, 110, 110],np.uint8)
yel2h = np.array([26, 255, 255], np.uint8)
pin1h = np.array([166, 170, 10],np.uint8)
pin2h = np.array([170, 255, 255], np.uint8)
pur1h = np.array([141, 100, 10],np.uint8)
pur2h = np.array([146, 240, 160], np.uint8)



while (True):  
    (video, cuadro) = camara.read() #  leemos la camara
    if not video:# Si hemos llegado al final del vídeo salimos
        break
    imgh = cv2.cvtColor(cuadro, cv2.COLOR_BGR2HSV)# Convertimos a HSV
    
    mask1 = cv2.inRange(imgh, red1h, red2h);
    mask2 = cv2.inRange(imgh, gre1h, gre2h);
    mask3 = cv2.inRange(imgh, blu1h, blu2h);
    mask4 = cv2.inRange(imgh, ora1h, ora2h);
    mask5 = cv2.inRange(imgh, yel1h, yel2h);
    mask6 = cv2.inRange(imgh, pin1h, pin2h);
    mask7 = cv2.inRange(imgh, pur1h, pur2h);
    
    maska = cv2.add(mask1, mask2)
    maskb = cv2.add(mask3, mask4)
    maskc = cv2.add(mask5, mask6)
    maskd = cv2.add(maska, maskb)
    maske = cv2.add(maskc, mask7)
    maskf = cv2.add(maskd, maske)
   
    
    maskv = cv2.bitwise_and(cuadro, cuadro, mask=maskf)
    
    
    
    cv2.imshow("video HSV 7 colores", maskv)
    cv2.imshow("video HSV", imgh)
   
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

camara.release()  # Liberamos la cámara 
cv2.destroyAllWindows() #cerramos todas las ventanas

camara = cv2.VideoCapture(0) # Cargamos el vídeo

# LAB
red1l = np.array([70, 160, 140],np.uint8)
red2l = np.array([130, 170, 155], np.uint8)
gre1l = np.array([70, 105, 135],np.uint8)
gre2l = np.array([150, 120, 245], np.uint8)
blu1l = np.array([40, 130, 90],np.uint8)
blu2l = np.array([55, 145, 110], np.uint8)
ora1l = np.array([90, 160, 150],np.uint8)
ora2l = np.array([210, 170, 160], np.uint8)
yel1l = np.array([135, 50, 165],np.uint8)
yel2l = np.array([150, 125, 195], np.uint8)
pin1l = np.array([100, 175, 120],np.uint8)
pin2l = np.array([240, 190, 140], np.uint8)
pur1l = np.array([50, 140, 110],np.uint8)
pur2l = np.array([160, 155, 130], np.uint8)

 
while (True):  
    (video, cuadro) = camara.read() #  leemos la camara
    if not video:# Si hemos llegado al final del vídeo salimos
        break
    imgl = cv2.cvtColor(cuadro, cv2.COLOR_BGR2LAB)# Convertimos a LAB
    
    mask1 = cv2.inRange(imgl, red1l, red2l);
    mask2 = cv2.inRange(imgl, gre1l, gre2l);
    mask3 = cv2.inRange(imgl, blu1l, blu2l);
    mask4 = cv2.inRange(imgl, ora1l, ora2l);
    mask5 = cv2.inRange(imgl, yel1l, yel2l);
    mask6 = cv2.inRange(imgl, pin1l, pin2l);
    mask7 = cv2.inRange(imgl, pur1l, pur2l);
    
    maska = cv2.add(mask1, mask2)
    maskb = cv2.add(mask3, mask4)
    maskc = cv2.add(mask5, mask6)
    maskd = cv2.add(maska, maskb)
    maske = cv2.add(maskc, mask7)
    maskf = cv2.add(maskd, maske)
    
    
    maskv = cv2.bitwise_and(cuadro, cuadro, mask=maskf)
    
    
    
    cv2.imshow("video LAB 7 colores", maskv)
    cv2.imshow("video LAB ", imgl)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    
camara.release()  # Liberamos la cámara 
cv2.destroyAllWindows() #cerramos todas las ventanas
