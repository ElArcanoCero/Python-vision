import tkinter as tk
from tkinter import messagebox, PhotoImage, Entry, StringVar, IntVar
import cv2
import ctypes
import os
from os import mkdir
from tkinter import font

# Función para la captura y guardado de datos faciales
def registro_facial():
    ventana2 = cv2.VideoCapture(0)  # Cámara predeterminada
    global n
    global direc
    n = 0
    num = 0
    texto = "   Mira la luz arriba"
    usuario_num = str(dato_numero1.get())    
    direc = os.path.join('C:/Users/Arcano/Desktop/python/diceno2/', usuario_num)  # Directorio donde se guardan las imágenes del usuario
    
    try:
        mkdir(direc)  # Crear la carpeta si no existe
    except FileExistsError:
        messagebox.showerror("Error", "La carpeta para este usuario ya existe.")
        return
    
    # Guardar datos del usuario en un archivo de texto
    with open(os.path.join(direc, 'datos.txt'), 'w') as archi1:
        archi1.write(f"{dato_nombre1.get()}\n")
        archi1.write(f"{dato_apellido1.get()}\n")
        archi1.write(f"{dato_numero1.get()}\n")
    
    user32 = ctypes.windll.user32
    ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
    while True:
        ret, frame = ventana2.read()
        if not ret:
            break
        
        (a, an) = frame.shape[:2]
        ancho2 = int((ancho - an) / 2)
        alto2 = int((alto - a) / 2)

        # Guardar imágenes después de la primera captura
        if n >= 10:
            cv2.imwrite(os.path.join(direc, f'img{n}.jpg'), frame)
            num += 1
        n += 1
        
        cv2.putText(frame, "Manten tu rostro dentro del ovalo", 
                    (100, a-30), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)
        a = int(a / 2)
        an = int(an / 2)
        cv2.ellipse(frame, (an, a), (100, 140), 0, 0, 360, (255, 0, 0), 3)
        cv2.putText(frame, texto, (135, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)
        
        cv2.imshow('Registro Facial', frame)
        cv2.moveWindow('Registro Facial', ancho2, alto2)
        ventana.withdraw()  # Ocultar ventana principal
        
        if num == 1:
            messagebox.showinfo(message="Mira la luz de color rojo, arriba\nPresiona espacio o enter para continuar", title="Advertencia")
        
        if num == 10:
            texto = "Mira la luz a la derecha"
            messagebox.showinfo(message="Mira la luz de color verde, a la derecha\nPresiona espacio o enter para continuar", title="Advertencia")
        
        if num == 20:
            texto = "   Mira la luz abajo"
            messagebox.showinfo(message="Mira la luz de color verde, abajo\nPresiona espacio o enter para continuar", title="Advertencia")
        
        if num == 30:
            texto = "  Mira la luz a la izquierda"
            messagebox.showinfo(message="Mira la luz de color verde, a la izquierda\nPresiona espacio o enter para continuar", title="Advertencia")
        
        if num >= 40:
            messagebox.showinfo(message="Gracias por realizar tu registro\nPresiona espacio o enter para continuar", title="Advertencia")
            break
        
        cv2.waitKey(30)
    
    ventana.deiconify()  # Mostrar la ventana principal de nuevo
    ventana2.release()  # Liberar la cámara
    cv2.destroyAllWindows()
    # Limpiar entradas
    dato_nombre1.delete(0, tk.END)
    dato_apellido1.delete(0, tk.END)
    dato_numero1.delete(0, tk.END)


# Función para habilitar botón de registro cuando los campos estén completos
def activar(*args):
    if dato_nombre1.get() and dato_apellido1.get() and dato_numero1.get():
        boton.configure(state=tk.NORMAL)
    else:
        boton.configure(state=tk.DISABLED)


# Configuración de la ventana principal y widgets
ventana = tk.Tk()
ventana.geometry("300x340")
ventana.title("Bot Industries")
ventana.config(bg="#2E2D2C")

# Icono de la ventana (reemplazar la ruta del archivo si es necesario)
icono = PhotoImage(file="C:/Users/Arcano/Desktop/python/diceno2/logo.png")
ventana.iconphoto(True, icono)

ventana.eval('tk::PlaceWindow . center')

# Variables para los datos del formulario
nombre1 = StringVar()
apellido1 = StringVar()
numero1 = IntVar(value='')

# Etiqueta del título
Label(ventana, text="Datos De Registro", bg="#1F1E1D", fg='#ad4545', width="300", height="2",
      font=font.Font(family="Times", size=14)).pack()

# Campos de entrada
Label(ventana, bg="#2E2D2C", fg='#ad4545', font=font.Font(family="Times", size=14), text="\nPrimer nombre * ").pack()
dato_nombre1 = Entry(ventana, textvariable=nombre1, bg='white', fg='black', font=font.Font(family="Times", size=14))
dato_nombre1.pack()

Label(ventana, bg="#2E2D2C", fg='#ad4545', font=font.Font(family="Times", size=14), text="Primer apellido * ").pack()
dato_apellido1 = Entry(ventana, textvariable=apellido1, bg='white', fg='black', font=font.Font(family="Times", size=14))
dato_apellido1.pack()

Label(ventana, bg="#2E2D2C", fg='#ad4545', font=font.Font(family="Times", size=14), text="Número de documento *").pack()
Label(ventana, bg="#2E2D2C", fg='#ad4545', font=font.Font(family="Times", size=10), text="(Sin espacios o signos)").pack()
dato_numero1 = Entry(ventana, textvariable=numero1, bg='white', fg='black', font=font.Font(family="Times", size=14))
dato_numero1.pack()

# Asociar la función `activar` para habilitar el botón si los campos están llenos
nombre1.trace_add("write", activar)
apellido1.trace_add("write", activar)
numero1.trace_add("write", activar)

# Botón para iniciar el registro facial
boton = tk.Button(ventana, text="Siguiente", bg="white", fg="#ad4545", height="2", width="20",
                  command=registro_facial, font=font.Font(family="Times", size=14), state=tk.DISABLED)
boton.pack()

ventana.mainloop()
