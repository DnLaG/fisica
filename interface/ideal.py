import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def crear_titulos_de_controles(variables):
    label = ttk.LabeledScale(variables, None, 0, 100)


def crear_controles(variables):
    var_x0 = ttk.Scale(variables, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_x0.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
    var_y0 = ttk.Scale(variables, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_y0.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
    var_z0 = ttk.Scale(variables, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_z0.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
    var_x = ttk.Scale(variables, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
    var_y = ttk.Scale(variables, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
    var_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
    var_z = ttk.Scale(variables, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
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
        variables.pack(side=tk.BOTTOM, fill=tk.BOTH, ipadx=5, ipady=5)

        # Añadir elementos de controles

        crear_titulos_de_controles(variables)
        crear_controles(variables)
