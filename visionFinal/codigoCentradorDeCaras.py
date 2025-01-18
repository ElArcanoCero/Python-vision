import tkinter as tk
from tkinter import *
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
#import os
from os import mkdir
#import numpy as np

ventana2 = cv2.VideoCapture(0)                #Elegimos la camara con la que vamos a hacer la deteccion
global n 
global direc
n = 0
usuario_num = str('987')    
direc =str('C:/Users/Arcano/OneDrive/Escritorio/pyton/visionFinal/dice2/'+usuario_num) # direccion de la carpeta donde se almacena cada usuario sengo su documento
mkdir(direc)                                  # creamos la carpeta
archi1=open(direc+'/datos.txt',"w")           # creamos el archivo txt
archi1.write(str('jose')+"\n")                # guardamos el nombre y cambiamos de renglon
archi1.write(str('restrepo')+"\n")            # guardamos apellido
archi1.write(str('987')+"\n")                 # guardamos el documento estos 3 se pueden hacer en una sola linea de codigo
  
while(True):
    ret, frame = ventana2.read()               # leemos el video
    cv2.imwrite(direc+'/img.jpg', frame)       # se guarda el cuadro en una imagen temporal
    img = direc+'/img.jpg'                     # direcion de la imagen
    pixeles = pyplot.imread(img)               # leemos la imagen en formato pyplot
    detector = MTCNN()                         # renombramos el dectector de caras
    caras = detector.detect_faces(pixeles)     # detectamos la cara
    x1, y1, x2, y2 = caras[0]['box']           # obtenemos los puntos de referencia para el cuadro de la cara
    a, an, c = frame.shape
    a = int(a/2)
    an = int(an/2)
    
    cv2.ellipse(frame, 
               (an, a), 
               (90, 140),
               0, 
               0,
               360,
               (0, 0, 255),
               3)
    
    cv2.rectangle(frame, 
                   (230, 150),
                   (270, 180),
                   (255, 0, 0), 
                   1) 
    
    cv2.rectangle(frame, 
                   (370, 150),
                   (410, 180),
                   (255, 0, 0), 
                   1) 
    
    cv2.rectangle(frame, 
                   (x1, y1),
                   (x1+x2, y1+y2),
                   (0, 255, 0), 
                   1) 
    
   
    
    cv2.imwrite(direc+'/img.jpg', frame)      # se guarda el cuadro en una imagen temporal
    cv2.imshow('imagen',frame)
    cv2.waitKey(120)
    #cv2.destroyAllWindows()
    
    if len(caras) == 1 :                      # aseguramos que en el cuadro solo se ve una cara
        if x1 >= 230 and x1 <= 270 and y1 >= 150 and y1 <= 180:  
            if x2 >= 100 and x2 <= 140 and y1 :
                #reg_rostro(img, caras) 
                n = n + 1
                
   
    
    if n >= 1:                                #se para la captura de imagenes al completar los ciclos
        break
    
