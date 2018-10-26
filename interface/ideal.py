import tkinter as tk
from tkinter import ttk


def boton_posicion():
    print("Click Botón Posición")


def boton_velocidad():
    pass


def boton_aceleracion():

    pass


def boton_alcance_horizontal():
    pass


def boton_altura_maxima():
    pass


def boton_camino_recorrido():
    pass


def boton_radio_y_centro_de_curvatura():
    pass


def boton_aceleracion_normal_y_tangencial():
    pass


def boton_vector_normal():
    pass



class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fisica")
        self.window.minsize(800, 600)
        self.window.maxsize(1280, 960)
        self.entrada_posicion_x0 = ttk.Entry()
        self.entrada_posicion_y0 = ttk.Entry()
        self.entrada_angulo_inicial = ttk.Entry()
        self.entrada_aceleracion_inicial = ttk.Entry()
        self.deslizador_posicion_x0 = ttk.Scale()
        self.deslizador_posicion_y0 = ttk.Scale()
        self.deslizador_angulo_inicial = ttk.Scale()
        self.deslizador_aceleracion_inicial = ttk.Scale()

        self.pestañas = ttk.Notebook(self.window)
        self.tab_ideal = ttk.Frame(self.pestañas)
        self.opciones = ttk.Frame(self.tab_ideal)

        # Inicializar los botones de la interfaz
        self.boton_posicion = ttk.Button(self.opciones, text="Posición", width=10, command=lambda: boton_posicion())
        self.boton_velocidad = ttk.Button(self.opciones, text="Velocidad", width=10, command=lambda: boton_velocidad())
        self.boton_aceleracion = ttk.Button(self.opciones, text="Aceleración", width=10, command=lambda: boton_aceleracion())
        self.boton_alcance_horizontal = ttk.Button(self.opciones, text="Alcance Horizontal", width=10, command=lambda: boton_alcance_horizontal())
        self.boton_altura_maxima = ttk.Button(self.opciones, text="Altura Màxima", width=10, command=lambda: boton_altura_maxima())
        self.boton_camino_recorrido = ttk.Button(self.opciones, text="Camino Recorrido", width=10, command=lambda: boton_camino_recorrido())
        self.boton_radio_y_centro_de_curvatura = ttk.Button(self.opciones, text="Radio y Centro de Curvatura", width=10, command=lambda: boton_radio_y_centro_de_curvatura())
        self.boton_aceleracion_normal_y_tangencial = ttk.Button(self.opciones, text="A. normal y tangencial", width=10, command=lambda: boton_aceleracion_normal_y_tangencial())
        self.boton_vector_normal = ttk.Button(self.opciones, text="Vector normal", width=10, command=lambda: boton_vector_normal())

        self.create_widgets()

    def create_widgets(self):

        def f_posicion_x0(event):
            print(posicion_x0.get())

        def f_posicion_y0(event):
            print(posicion_y0.get())

        def f_angulo_inicial(event):
            print(angulo_inicial.get())

        def f_aceleracion_inicial(event):
            print(aceleracion_inicial.get())

        # Limpia Entry iniciales, de modo que al hacer click estos se vacian
        def limpiar_entrada_x0(event):
            if self.entrada_posicion_x0.get() == "X0":
                self.entrada_posicion_x0.delete(0,'end')

        def limpiar_entrada_y0(event):
            if self.entrada_posicion_y0.get() == "Y0":
                self.entrada_posicion_y0.delete(0,'end')

        def limpiar_entrada_angulo(event):
            if self.entrada_angulo_inicial.get() == "Angulo":
                self.entrada_angulo_inicial.delete(0,'end')

        def limpiar_entrada_aceleracion(event):
            if self.entrada_aceleracion_inicial.get() == "Aceleración":
                self.entrada_aceleracion_inicial.delete(0,'end')

        # Variables de los deslizadores
        posicion_x0 = tk.IntVar()
        posicion_y0 = tk.IntVar()
        angulo_inicial = tk.IntVar()
        aceleracion_inicial = tk.IntVar()
        self.pestañas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)

        tab_balistica = tk.Frame(self.pestañas)
        tab_seguridad = tk.Frame(self.pestañas)

        self.pestañas.add(self.tab_ideal, text="Movimiento Ideal", compound=tk.TOP)
        self.pestañas.add(tab_seguridad, text="Parabola de Seguridad", compound=tk.TOP)
        self.pestañas.add(tab_balistica, text="Movimiento Balistico", compound=tk.TOP)


        # tutorial = ttk.LabelFrame(self.window, text="Instrucciones")
        # tutorial.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=10, pady=10)

        self.opciones.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=5, pady=5)

        self.boton_posicion.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_velocidad.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_aceleracion.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_alcance_horizontal.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_altura_maxima.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_camino_recorrido.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_radio_y_centro_de_curvatura.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_aceleracion_normal_y_tangencial.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_vector_normal.pack(side=tk.TOP, padx=10, pady=10)

        graphics = ttk.LabelFrame(self.tab_ideal, text="Gráfica")
        graphics.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        separador = ttk.Separator(self.tab_ideal, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)

        variables = ttk.LabelFrame(self.tab_ideal, text="Controles")
        variables.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        # Contenedores de los controles
        posicion = ttk.Frame(variables)
        posicion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        angulo = ttk.Frame(variables)
        angulo.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        aceleracion = ttk.Frame(variables)
        aceleracion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        # Añadir elementos de entrada de texto
        self.entrada_posicion_x0 = ttk.Entry(posicion, justify=tk.CENTER)
        self.entrada_posicion_x0.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_posicion_x0.insert(tk.END, "X0")
        self.entrada_posicion_x0.bind("<Button-1>", limpiar_entrada_x0)

        self.entrada_posicion_y0 = ttk.Entry(posicion, justify=tk.CENTER)
        self.entrada_posicion_y0.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_posicion_y0.insert(tk.END, "Y0")
        self.entrada_posicion_y0.bind("<Button-1>", limpiar_entrada_y0)

        self.entrada_angulo_inicial = ttk.Entry(angulo, justify=tk.CENTER)
        self.entrada_angulo_inicial.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_angulo_inicial.insert(tk.END, "Angulo")
        self.entrada_angulo_inicial.bind("<Button-1>", limpiar_entrada_angulo)

        self.entrada_aceleracion_inicial = ttk.Entry(aceleracion, justify=tk.CENTER)
        self.entrada_aceleracion_inicial.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_aceleracion_inicial.insert(tk.END, "Aceleración")
        self.entrada_aceleracion_inicial.bind("<Button-1>", limpiar_entrada_aceleracion)

        # Añadir elementos deslizadores para actualizar datos
        self.deslizador_posicion_x0 = ttk.Scale(posicion, variable=posicion_x0,  from_=0, to=100, orient=tk.HORIZONTAL)
        self.deslizador_posicion_x0.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_posicion_x0.set(50)
        self.deslizador_posicion_x0.bind("<B1-Motion>", f_posicion_x0)
        self.deslizador_posicion_x0.bind("<ButtonRelease-1>", f_posicion_x0)

        self.deslizador_posicion_y0 = ttk.Scale(posicion, variable=posicion_y0, from_=0, to=100, orient=tk.HORIZONTAL)
        self.deslizador_posicion_y0.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_posicion_y0.set(50)
        self.deslizador_posicion_y0.bind("<B1-Motion>", f_posicion_y0)
        self.deslizador_posicion_y0.bind("<ButtonRelease-1>", f_posicion_y0)

        self.deslizador_angulo_inicial = ttk.Scale(angulo, variable=angulo_inicial, from_=0, to=90, orient=tk.HORIZONTAL)
        self.deslizador_angulo_inicial.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_angulo_inicial.set(180)
        self.deslizador_angulo_inicial.bind("<B1-Motion>", f_angulo_inicial)

        self.deslizador_aceleracion_inicial = ttk.Scale(aceleracion, variable=aceleracion_inicial, from_=0, to=100, orient=tk.HORIZONTAL)
        self.deslizador_aceleracion_inicial.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_aceleracion_inicial.set(50)
        self.deslizador_aceleracion_inicial.bind("<B1-Motion>", f_aceleracion_inicial)
        self.deslizador_aceleracion_inicial.bind("<ButtonRelease-1>", f_aceleracion_inicial)



    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_position_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_angle_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_acceleration_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())
