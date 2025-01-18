import tkinter as tk
from tkinter import *
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import os
from os import mkdir
import threading
import time


    
# abre camara y guarda datos del reconocimiento facial

def registro_facial():
   
    global direc
    usuario_num = str(dato_numero1.get())    
    direc =str('C:/Users/Arcano/Desktop/python/diceno2/'+usuario_num) # direccion de la carpeta donde se almacena cada usuario sengo su documento
    mkdir(direc)  # creamos la carpeta
    archi1=open(direc+'/datos.txt',"w") # creamos el archivo txt
    archi1.write(str(dato_nombre1.get())+"\n")  # guardamos el nombre y cambiamos de renglon
    archi1.write(str(dato_apellido1.get())+"\n") # guardamos apellido
    archi1.write(str(dato_numero1.get())+"\n")  # guardamos el documento estos 3 se pueden hacer en una sola linea de codigo

    def hilo(i):
        n=0
        cont = 0  
        ventana2 = cv2.VideoCapture(0)  #Elegimos la camara con la que vamos a hacer la deteccion
                
        if i == 0:
            while (ventana2.isOpened()):

                ret, frame = ventana2.read() 
                if n >= 30:
                    cv2.imwrite(direc+'/img.jpg', frame)  # se guarda el cuadro en una imagen temporal
                    n=0
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
                texto = "mira hacia la luz"
                tamañoLetra = 1
                colorLetra = (221,0,0)
                grosorLetra = 1
                cv2.putText(frame,
                texto, 
                (100,30),
                cv2.FONT_HERSHEY_TRIPLEX,
                1,
                (221,0,0),
                1)
                cv2.imshow('Cam',frame)
                n=n+1
                cont = os.listdir(direc)
                cv2.waitKey(30)    
                if len(cont) >= 4: # cierra la camara cuando se cumpla el nuemro de archivos
                   ventana2.release()   
                   cv2.destroyAllWindows()
                   break
               
       
        if i == 1:
            while(len(os.listdir(direc))<=1):# no permite que incie el segundo hila hasta que tenaga la imagen temporal
                time.sleep(1) 
                print('hola') 
            while (True):  
                img = direc+'/img.jpg' # direcion de la imagen
                imgp = pyplot.imread(img)  # leemos la imagen en formato pyplot
                cara = MTCNN().detect_faces(imgp) # detectamos la cara
                x1, y1, x2, y2 = cara[0]['box'] # obtenemos los puntos de referencia para el cuadro de la cara
                if len(cara) == 1 : # aseguramos que en el cuadro solo se ve una cara
                    if x1 >= 200 and x1 <= 300 and y1 >= 100 and y1 <= 200:  
                        if x2 >= 100 and x2 <= 140 and y2 >= 100 and y2 <= 200:
                            imgp = cv2.cvtColor(imgp, cv2.COLOR_BGR2RGB)# cambio el espacio de color
                            x3,y3 = x1+x2, y1+y2
                            pyplot.subplot(1, len(cara), 1)
                            pyplot.axis('off')
                            imgp_rec = imgp[y1-15:y3+15, x1-15:x3+15]                   
                            #imgp_rec = cv2.resize(imgp_rec, no creo que debamos deformar las imagenes
                            #(255,255), 
                            #interpolation = cv2.INTER_CUBIC) # guardamos la imagen con un tamaño de 255 x 255 pixeles   
                            #cv2.imwrite(direc+'/img.jpg', imgp_rec)
                            cv2.imwrite(direc+'/img'+str(n)+'.jpg', imgp_rec)
                            n = n + 1 
                            print(n)  
                                
                if n >= 3: 
                    break    
        print(i)                
    
    simplethread=[] 
    for i in range(2):#iniciamos los hilos
        simplethread.append(threading.Thread(target=hilo, args=[i])) 
        simplethread[-1].start() 

    for i in range(2):     
        simplethread[i].join() # esperamos que acabe el hilo num i
    
    dato_nombre1.delete(0, END)  
    dato_apellido1.delete(0, END)
    dato_numero1.delete(0, END)
        
def activar(*args):
    
    text1 = dato_nombre1.get().lower()
    text2 = dato_apellido1.get().lower()
    text3 = dato_numero1.get().lower()
    
    if text1 != '' :
        if text2 != '':
            if text3 != '':
                boton.configure(state = NORMAL)
       
    else : boton.configure(state = DISABLED)
    
#contenedor datos de usuario 
    
global nombre1      #Globalizamos la variable para usarla en las funciones
global dato_nombre1
global apellido1
global dato_apellido1
global numero1
global dato_numero1
global boton
    
ventana = Tk()
ventana.geometry("300x250")  #Asignamos el tamaño a la ventana 
ventana.title("bot Industries")  #Asignamos el titulo a la ventana
icono = PhotoImage(file ="C:/Users/Arcano/Desktop/python/diceno2/logo.png") # ubicacion del icono
ventana.iconphoto(True, icono)  # activo el icono

Label(text = "datos de registro",
        bg = "white", 
        width = "300",
        height = "2", 
        font = ("Verdana", 13)).pack()  #caracteristicas de la ventana

nombre1 = StringVar()   #creo las variables asignando un tipo de dato
apellido1 = StringVar()
numero1 = IntVar(value= '')
   
# datos de formulario
    
Label(ventana, text = "primer nombres * ").pack()    
dato_nombre1 = Entry(ventana, textvariable = nombre1)
dato_nombre1.pack()
    
    
Label(ventana, text = "primer pellidos * ").pack()
dato_apellido1 = Entry(ventana, textvariable = apellido1)
dato_apellido1.pack()
   
Label(ventana, text = "numero de documento * ").pack()
dato_numero1 = Entry(ventana, textvariable = numero1)
dato_numero1.pack()
    
nombre1.trace_add("write", activar)
apellido1.trace_add("write", activar)
numero1.trace_add("write", activar)
    
Label(text = "").pack() #Creamos el espacio entre el label y el boton
boton = tk.Button(text = "siguiente", 
                height = "2", 
                width = "20", 
                command = registro_facial, 
                #font = 'bold 10',
                state=tk.DISABLED) #caracteristicas del boton que debe tener un mejor nombre

boton.pack()    

ventana.mainloop()