"""
    Version Sofware: 0.0.0
    Version Python: 3.7
"""

import main
import tkinter as tk
import ideal as id
import balistico as bl

class menu():
    propiedades = main.propiedades() #Importando propiedades del proyecto
    ventana = tk.Tk()
    ventana.title(propiedades.version)
    ventana.mainloop()
