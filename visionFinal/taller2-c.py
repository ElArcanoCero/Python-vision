from matplotlib.pyplot import pause
import numpy as np
import cv2

# Cargamos el vídeo
camara = cv2.VideoCapture(0)
toma1  = None # creamos un cuadro a vacío.
toma2  = None # creamos un cuadro a vacío.
toma3  = None # creamos un cuadro a vacío.
n = 0
band = 0
while (True):  
	toma2 = toma1
	#  leemos la camara
	(grabbed, cuadro) = camara.read()
	if not grabbed:# Si hemos llegado al final del vídeo salimos
		break
	imgv = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)# Convertimos a escala de grises
	imgvg = cv2.GaussianBlur(imgv, (91, 91), 0)# Aplicamos suavizado para eliminar ruido
	#imgvgb = cv2.threshold(imgvg, 120, 255, cv2.THRESH_BINARY)[1] #binariso a imgvg
	
  
	if toma1 is None:# llenamos el primer cuadro con la primera imagen tomada
		toma1 = imgvg
		#calculamos el histograma de ambas imagenes
		img1h = cv2.calcHist([imgvg], [0], None, [256], [0, 256])
		img2h = cv2.calcHist([toma1], [0], None, [256], [0, 256])
	else:
		toma1 = imgvg
		#calculamos el histograma de ambas imagenes
		img1h = cv2.calcHist([imgvg], [0], None, [256], [0, 256])
		img2h = cv2.calcHist([toma2], [0], None, [256], [0, 256])
    
	
	#Calculamos la correlación que hay entre el fondo y los siguientes cuadros
	corre=cv2.compareHist(img1h,img2h,cv2.HISTCMP_CORREL)
	
	if (band == 0):
		corre1 = corre - 0.003
		band = 1
	
	
	if (corre <= corre1):
		n = n+1
		print("movimiento en el area", n)
		print(corre)
		print(corre1)
     
	# Mostramos las imágenes de la cámara, el fondo y umbral binzarizado
	cv2.imshow("imagen 1", imgvg)
	cv2.imshow("imagen 2", toma1)
	cv2.imshow("video", cuadro)
	
	if cv2.waitKey(1) & 0xFF == ord('s'):
		break
# Liberamos la cámara y cerramos todas las ventanas
camara.release()
cv2.destroyAllWindows()