import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def crear_titulos_de_controles(posicion, angulo, aceleracion):
    texto_variable = tk.StringVar()
    posicion_entry = ttk.Entry(posicion, width=15, justify=tk.CENTER)
    posicion_entry.pack(side=tk.TOP)
    posicion_entry.insert(tk.END, "Posición inicial")

    angulo_entry = ttk.Entry(angulo, width=15, justify=tk.CENTER)
    angulo_entry.pack(side=tk.TOP)
    angulo_entry.insert(tk.END, "Angulo")

    aceleracion_entry = ttk.Entry(aceleracion, width=15, justify=tk.CENTER)
    aceleracion_entry.pack(side=tk.TOP)
    aceleracion_entry.insert(tk.END, "Aceleracion inicial")


def crear_controles(posicion, movimiento, aceleracion):
    var_x = ttk.Scale(posicion, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
    var_y = ttk.Scale(movimiento, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
    var_z = ttk.Scale(aceleracion, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_z.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)


class Interface():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fisica")
        self.window.minsize(800, 600)
        self.window.maxsize(1280, 960)
        self.create_widgets()

    def create_widgets(self):
        tab_frame = ttk.Notebook(self.window)
        tab_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)

        tab_ideal = tk.Frame(tab_frame)
        tab_balistica = tk.Frame(tab_frame)
        tab_seguridad = tk.Frame(tab_frame)

        tab_frame.add(tab_ideal, text="Movimiento Ideal", compound=tk.TOP)
        tab_frame.add(tab_balistica, text="Movimiento Balistico", compound=tk.TOP)
        tab_frame.add(tab_seguridad, text="Parabola Seguridad", compound=tk.TOP)

        # tutorial = ttk.LabelFrame(self.window, text="Instrucciones")
        # tutorial.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=10, pady=10)

        graphics = ttk.LabelFrame(tab_ideal, text="Movimiento Ideal")
        graphics.pack(side=tk.TOP, fill=tk.BOTH, expand=True, ipadx=5, ipady=5)

        separador = ttk.Separator(tab_ideal, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, ipady=10, fill=tk.X)

        variables = ttk.LabelFrame(tab_ideal, text="Controles")
        variables.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipadx=5, ipady=5)

        posicion = ttk.Frame(variables)
        posicion.pack(side=tk.TOP)
        movimiento = ttk.Frame(variables)
        movimiento.pack(side=tk.TOP)
        aceleracion = ttk.Frame(variables)
        aceleracion.pack(side=tk.TOP)

        # Añadir elementos de controles

        crear_titulos_de_controles(posicion, movimiento, aceleracion)
        crear_controles(posicion, movimiento, aceleracion)
