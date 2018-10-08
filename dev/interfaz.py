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
    
    def __init__(self, master=None): #Master es la ventana y self es el frame
        super().__init__(master)
        master.title(self.propiedades.version)
        master.config(bg="white")
        master.config(relief="flat", bd=8) #tipo de borde relief y bd es la 
        
        self.pack(fill = "both", expand="true") #Empaquetamos el frame
        self.config(bg = "#bfbfbf", width = self.propiedades.default_size_ancho, height = self.propiedades.default_size_alto) #Medidas iniciales de la ventana + Color de fondo
        
ventana = tk.Tk()
menu_root = menu(master = ventana)
ventana.mainloop()
            
