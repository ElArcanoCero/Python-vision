import numpy as np
import cv2


camara = cv2.VideoCapture(0) # Cargamos el vídeo


tam = 90

while (True):  
    (video, cuadro) = camara.read() #  leemos la camara
    if not video:# Si hemos llegado al final del vídeo salimos
        break
    hei, wid = cuadro .shape[:2]  # Obtenemos sus dimensiones
    
    
   
    cuadro[hei//2:hei//2+1, 0 : (wid//2)-tam] = [0,0,255]
    cuadro[hei//2:hei//2+1, (wid//2)+tam+1 : wid] = [0,0,255]
    cuadro[0 : (hei//2)-tam,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[(hei//2)+tam+1 : hei ,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[(hei//2)-5 : (hei//2)+6 ,wid//2 : wid//2+1] = [0, 0, 255]
    cuadro[hei//2:hei//2+1, (wid//2)-5 : (wid//2)+6] = [0,0,255]
    cv2.rectangle(cuadro, (wid//2-tam,hei//2-tam), (wid//2+tam+1,hei//2+tam+1), (0,0,255)) # enmarco la zona donde se realizara la lectura
    
    cv2.putText(cuadro, 'centra la imagen', ((wid//2)-tam-50, (hei//2)-tam-10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
      
    punt1 = [0,0]
    punt2 = [0,0]
    punt3 = [0,0]
    punt4 = [0,0] 
     
    imgr = cuadro[hei//2-tam:hei//2+tam, wid//2-tam:wid//2+tam]  # recorta un recuadro en el cenmtro de la imagen
    imgr = cv2.cvtColor(imgr, cv2.COLOR_BGR2GRAY)  # Conversion a escala de grises
    imgg = cv2.GaussianBlur(imgr, (3, 3), 0)# Aplicamos suavizado para eliminar ruido
    imgc = cv2.Canny(imgg, 60, 200) #filtro canny
    imgc= cv2.threshold(imgc, 120, 255, cv2.THRESH_BINARY)[1] #binariso 
    imgs = (np.ones((180, 180), np.uint8))*255 # imagen en blanco para salida

    mat1 =[[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 255, 255, 255],
            [0, 0, 255, 0, 0],
            [0, 0, 255, 0, 0]]

    mat2 =[[0, 0, 255, 0, 0],
           [0, 0, 255, 0, 0],
           [0, 0, 255, 255, 255],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

    mat3 =[[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [255, 255, 255, 0, 0],
            [0, 0, 255, 0, 0],
            [0, 0, 255, 0, 0]]

    mat4 =[[0, 0, 255, 0, 0],
            [0, 0, 255, 0, 0],
            [255, 255, 255, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    mat5 = [[0, 0, 0],
            [0, 255, 255],
            [0, 255, 0]]

    mat6 = [[0, 255, 0],
            [0, 255, 255],
            [0, 0, 0]]
    
    mat7 = [[0, 0, 0],
            [255, 255, 0],
            [0, 255, 0]]
    
    mat8 = [[0, 255, 0],
            [255, 255, 0],
            [0, 0, 0]]
    
    
                
    for i in range(2, 180-2):
        if((any(imgc[i,:])== True)):
            for j in range(2, 180-2):
                if ((imgc[i,j])== 255):
                    
                    mat = [[imgc[i-2,j-2], imgc[i-2,j-1], imgc[i-2,j], imgc[i-2,j+1], imgc[i-2, j+2]],
                        [imgc[i-1,j-2], imgc[i-1,j-1], imgc[i-1,j], imgc[i-1,j+1], imgc[i-1, j+2]],
                        [imgc[i,j-2], imgc[i,j-1], imgc[i,j], imgc[i,j+1], imgc[i, j+2]],
                        [imgc[i+1,j-2], imgc[i+1,j-1], imgc[i+1,j], imgc[i+1,j+1], imgc[i+1, j+2]],
                        [imgc[i+2,j-2], imgc[i+2,j-1], imgc[i+2,j], imgc[i+2,j+1], imgc[i+2, j+2]]]
                    
                    mat9 = [[imgc[i-1,j-1], imgc[i-1,j], imgc[i-1,j+1]],
                            [imgc[i,j-1], imgc[i,j], imgc[i,j+1]],
                            [imgc[i+1,j-1], imgc[i+1,j], imgc[i+1,j+1]]]
                    
                    esq1 = np.allclose(mat1, mat, rtol=1e-01, atol=1e-01, equal_nan=False)
                    esq2 = np.allclose(mat2, mat, rtol=1e-01, atol=1e-01, equal_nan=False)
                    esq3 = np.allclose(mat3, mat, rtol=1e-01, atol=1e-01, equal_nan=False)
                    esq4 = np.allclose(mat4, mat, rtol=1e-01, atol=1e-01, equal_nan=False)
                    esq5 = np.allclose(mat5, mat9, rtol=1e-01, atol=1e-01, equal_nan=False)
                    esq6 = np.allclose(mat6, mat9, rtol=1e-01, atol=1e-01, equal_nan=False)
                    esq7 = np.allclose(mat6, mat9, rtol=1e-01, atol=1e-01, equal_nan=False)
                    esq8 = np.allclose(mat8, mat9, rtol=1e-01, atol=1e-01, equal_nan=False) 
                    
                    if (esq1 == True or esq5 == True ): 
                        punt1[0] = i
                        punt1[1] = j
                        imgs[i,j]= 0
                        imgs[i,j+1] = 0
                        imgs[i+1,j] = 0
                        imgs[i,j+2] = 0
                        imgs[i+2,j] = 0

                    if (esq2 == True or esq6 == True): 
                     
                        punt2[0] = i
                        punt2[1] = j
                        imgs[i,j]=0
                        imgs[i,j+1] = 0
                        imgs[i-1,j] = 0  
                        imgs[i,j+2] = 0
                        imgs[i-2,j] = 0  
                        
                    
                    if (esq3 == True or esq7 == True ): 
                        
                        punt3[0] = i
                        punt3[1] = j
                        imgs[i,j]=0
                        imgs[i,j-1] = 0
                        imgs[i+1,j] = 0 
                        imgs[i,j-2] = 0
                        imgs[i+2,j] = 0   
                                                            
                    if (esq4 == True  or esq8 == True): 
                        
                        punt4[0] = i
                        punt4[1] = j
                        imgs[i,j]=0
                        imgs[i,j-1] = 0
                        imgs[i-1,j] = 0  
                        imgs[i,j-2] = 0
                        imgs[i-2,j] = 0 
                        
    if( punt1[0] != 0 and punt2[0] != 0 and punt3[0] != 0 and punt4[0] != 0): 
        
        #if (punt1[0] <= punt2[0]+2 and punt1[0] >= punt2[0]-2):
               
        cv2.putText(cuadro, 'rectangulo detectado', ((wid//2)-tam-90, (hei//2)+tam+50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)          
                    
                        
                
                    
                  
    cv2.imshow("video 1", cuadro)
    cv2.imshow("video 2", imgs)
    cv2.imshow("video 3", imgc)
    
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    
camara.release()  # Liberamos la cámara 
cv2.destroyAllWindows() #cerramos todas las ventanas

    