"""
    Version Sofware: 0.0.0
    Version Python: 3.7
"""

import main
import tkinter as tk
import ideal as id
import balistico as bl

class menu(tk.Frame):
    propiedades = main.propiedades() #Importando propiedades del proyecto
    ventana = tk.Tk()
    ventana.title(propiedades.version)
    ventana.config(bg="white")
    ventana.config(relief="flat", bd=8) #tipo de borde relief y bd es la medida

    frame = tk.Frame(ventana) #Creamos un frame el cual pertenece a ventana
    frame.pack(fill = "both", expand="true") #Empaquetamos el frame
    frame.config(bg = "#bfbfbf", width = propiedades.default_size_ancho, height = propiedades.default_size_alto) #Medidas iniciales de la ventana + Color de fondo
    ventana.mainloop()
