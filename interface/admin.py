import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Interface():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fisica")
        self.window.minsize(360, 640)
        self.window.maxsize(720, 1280)
        self.create_widgets()

    def create_widgets(self):
        ideal_button = ttk.Button(self.window, text="Movimiento Ideal")
        ideal_button.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        balistico_button = ttk.Button(self.window, text="Movimiento Balistico")
        balistico_button.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        seguridad_button = ttk.Button(self.window, text="Parabola Seguridad")
        seguridad_button.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)