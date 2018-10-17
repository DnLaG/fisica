import tkinter as tk
from tkinter import ttk

def update_position_value(event):
    print(event.widget.get())


def update_angle_value(event):
    print(event.widget.get())


def update_acceleration_value(event):
    print(event.widget.get())


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

        graphics = ttk.LabelFrame(tab_ideal, text="Gráfica")
        graphics.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        separador = ttk.Separator(tab_ideal, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)

        variables = ttk.LabelFrame(tab_ideal, text="Controles")
        variables.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        # Contenedores de los controles
        posicion = ttk.Frame(variables)
        posicion.pack(side=tk.LEFT, padx=5, pady=5)

        angulo = ttk.Frame(variables)
        angulo.pack(side=tk.LEFT, padx=5, pady=5)

        aceleracion = ttk.Frame(variables)
        aceleracion.pack(side=tk.LEFT, padx=5, pady=5)

        # Añadir elementos de entrada de texto
        posicion_entry = ttk.Entry(posicion, width=15, justify=tk.CENTER)
        posicion_entry.pack(side=tk.TOP)
        posicion_entry.insert(tk.END, "Posición inicial")
        var_x = ttk.Scale(posicion, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        var_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
        var_x.set(50)
        var_x.bind("<B1-Motion>", update_position_value)
        var_x.bind("<ButtonRelease-1>", update_position_value)

        angulo_entry = ttk.Entry(angulo, width=15, justify=tk.CENTER)
        angulo_entry.pack(side=tk.TOP)
        angulo_entry.insert(tk.END, "Angulo")
        var_y = ttk.Scale(angulo, from_=0, to=360, orient=tk.HORIZONTAL, length=100)
        var_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
        var_y.set(180)
        var_y.bind("<B1-Motion>", update_angle_value)
        var_y.bind("<ButtonRelease-1>", update_angle_value)

        aceleracion_entry = ttk.Entry(aceleracion, width=15, justify=tk.CENTER)
        aceleracion_entry.pack(side=tk.TOP)
        aceleracion_entry.insert(tk.END, "Aceleración")
        var_y = ttk.Scale(aceleracion, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        var_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
        var_y.set(50)
        var_y.bind("<B1-Motion>", update_acceleration_value)
        var_y.bind("<ButtonRelease-1>", update_acceleration_value)
