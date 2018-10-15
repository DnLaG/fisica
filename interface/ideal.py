import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Interface():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fisica")
        self.window.minsize(800, 600)
        self.window.maxsize(1280, 960)
        self.create_widgets()

    def create_widgets(self):
        tab_frame = ttk.Notebook(self.window)
        tab_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tab_ideal = tk.Frame(tab_frame)
        tab_balistica = tk.Frame(tab_frame)
        tab_seguridad = tk.Frame(tab_frame)

        tab_frame.add(tab_ideal, text="Movimiento Ideal", compound=tk.TOP)
        tab_frame.add(tab_balistica, text="Movimiento Balistico", compound=tk.TOP)
        tab_frame.add(tab_seguridad, text="Parabola Seguridad", compound=tk.TOP)

        # tutorial = ttk.LabelFrame(self.window, text="Instrucciones")
        # tutorial.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=10, pady=10)

        graphics = ttk.LabelFrame(tab_ideal, text="Movimiento Ideal")
        graphics.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        variables = ttk.LabelFrame(tab_ideal, text="Controles")
        variables.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Añadir elementos de controles

        self.crear_controles(variables)

    def crear_controles(self, variables):
        my_scale = ttk.Scale(variables, from_=0, to=100, orient=tk.HORIZONTAL, length=200)
        my_scale.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)


