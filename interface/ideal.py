import tkinter as tk # ejecutar "sudo apt-get install python3-tk" si hay problemas con la importac
from tkinter import ttk
import numpy as np
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

class Interface:
    def __init__(self):
        # Valores Iniciales
        self.gravedad = 9.8
        self.velocidad_inicial = 10
        self.angulo = np.radians(2)
        self.x0 = 5
        self.y0 = 8
        self.z0 = 0
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
        self.graphics = ttk.LabelFrame(self.tab_ideal, text="Gráfica")

        self.figura = Figure(figsize=(4, 3), dpi=100)  # define la proporcion del gráfico
        self.ecuacion = np.arange(0, 10, .01)
        self.figura.add_subplot(111).plot(self.ecuacion, self.ecuacion * self.ecuacion)
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.graphics)
        self.canvas.draw()
        self.canvas = self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


        # Inicializar los botones de la interfaz
        self.boton_posicion = ttk.Button(self.opciones, text="Posición", width=10, command=lambda: self.boton_posicionf())
        self.boton_velocidad = ttk.Button(self.opciones, text="Velocidad", width=10, command=lambda: self.boton_velocidadf())
        self.boton_aceleracion = ttk.Button(self.opciones, text="Aceleración", width=10, command=lambda: self.boton_aceleracionf())
        self.boton_alcance_horizontal = ttk.Button(self.opciones, text="Alcance Horizontal", width=10, command=lambda: self.boton_alcance_horizontalf())
        self.boton_altura_maxima = ttk.Button(self.opciones, text="Altura Màxima", width=10, command=lambda: self.boton_altura_maximaf())
        self.boton_camino_recorrido = ttk.Button(self.opciones, text="Camino Recorrido", width=10, command=lambda: self.boton_camino_recorridof())
        self.boton_radio_y_centro_de_curvatura_circulo_obsculador = ttk.Button(self.opciones, text="Radio y Centro de Curvatura y Circulo Obsculador", width=10, command=lambda: self.boton_radio_y_centro_de_curvatura_circulo_obsculadorf())
        self.boton_aceleracion_normal_y_tangencial = ttk.Button(self.opciones, text="A. normal y tangencial", width=10, command=lambda: self.boton_aceleracion_normal_y_tangencialf())
        self.boton_vector_normal = ttk.Button(self.opciones, text="Vector normal", width=10,
                                              command=lambda: self.boton_vector_normalf())
        #self.boton_circulo_osculador = ttk.Button(self.opciones, text="Circulo Osculador", width=10,
                                              #command=lambda: self.boton_circulo_osculadorf())

        self.create_widgets()

    def create_widgets(self):

        def f_posicion_x0(event):
            print(posicion_x0.get())

        def f_posicion_y0(event):
            print(posicion_y0.get())

        def f_angulo_inicial(event):
            print(angulo_inicial.get())

        def f_Rapidez_inicial(event):
            print(Rapidez_inicial.get())

        # Limpia Entry iniciales, de modo que al hacer click estos se vacian
        def limpiar_entrada_x0(event):
            if self.entrada_posicion_x0.get() == "X0":
                self.entrada_posicion_x0.delete(0,'end')

        def update_x0(event):
            # todo ecuacion que se actualiza automatricamente
            input_x0 = self.entrada_posicion_x0.get()
            if input_x0 == '':
                input_x0 = 0
                self.actualizar_grafico(self.ecuacion * float(5),8,8,8)
            self.actualizar_grafico(self.ecuacion * float(5),8,8,8)

        def limpiar_entrada_y0(event):
            if self.entrada_posicion_y0.get() == "Y0":
                self.entrada_posicion_y0.delete(0,'end')

        def limpiar_entrada_angulo(event):
            if self.entrada_angulo_inicial.get() == "Angulo":
                self.entrada_angulo_inicial.delete(0,'end')

        def limpiar_entrada_Rapidez(event):
            if self.entrada_Rapidez_inicial.get() == "Rapidez Inicial":
                self.entrada_Rapidez_inicial.delete(0,'end')




        # Variables de los deslizadores
        posicion_x0 = tk.IntVar()
        posicion_y0 = tk.IntVar()
        angulo_inicial = tk.IntVar()
        Rapidez_inicial = tk.IntVar()
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
        self.boton_radio_y_centro_de_curvatura_circulo_obsculador.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_aceleracion_normal_y_tangencial.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_vector_normal.pack(side=tk.TOP, padx=10, pady=10)
        #self.boton_circulo_osculador.pack(side=tk.TOP, padx=10, pady=10)


        self.graphics.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        separador = ttk.Separator(self.tab_ideal, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)

        variables = ttk.LabelFrame(self.tab_ideal, text="Controles")
        variables.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        # Contenedores de los controles
        posicion = ttk.Frame(variables)
        posicion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        Rapidez = ttk.Frame(variables)
        Rapidez.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        angulo = ttk.Frame(variables)
        angulo.pack(side=tk.LEFT, expand=True, padx=5, pady=5)


        #todo añadir titulos
        self.entrada_posicion_x0 = ttk.Entry(posicion, justify=tk.CENTER)
        self.entrada_posicion_x0.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_posicion_x0.insert(tk.END, "0")
        self.entrada_posicion_x0.bind("<Button-1>", limpiar_entrada_x0)
        self.entrada_posicion_x0.bind("<Key>", update_x0)

        self.entrada_posicion_y0 = ttk.Entry(posicion, justify=tk.CENTER)
        self.entrada_posicion_y0.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_posicion_y0.insert(tk.END, "0")
        self.entrada_posicion_y0.bind("<Button-1>", limpiar_entrada_y0)

        # todo titulos para rapidez inicial
        self.entrada_Rapidez_inicial = ttk.Entry(Rapidez, justify=tk.CENTER)
        self.entrada_Rapidez_inicial.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_Rapidez_inicial.insert(tk.END, "Rapidez Inicial")
        self.entrada_Rapidez_inicial.bind("<Button-1>", limpiar_entrada_Rapidez)

        # todo titulos para angulo inicial
        self.entrada_angulo_inicial = ttk.Entry(angulo, justify=tk.CENTER)
        self.entrada_angulo_inicial.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_angulo_inicial.insert(tk.END, "Angulo Inicial")
        self.entrada_angulo_inicial.bind("<Button-1>", limpiar_entrada_angulo)


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

        self.deslizador_Rapidez_inicial = ttk.Scale(Rapidez, variable=Rapidez_inicial, from_=0, to=100, orient=tk.HORIZONTAL)
        self.deslizador_Rapidez_inicial.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_Rapidez_inicial.set(50)
        self.deslizador_Rapidez_inicial.bind("<B1-Motion>", f_Rapidez_inicial)
        self.deslizador_Rapidez_inicial.bind("<ButtonRelease-1>", f_Rapidez_inicial)

        #Insercion Grafico en la zona indicada


    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_position_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_angle_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_acceleration_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())
    # Declaracion de botones0
    def boton_posicionf(self):
        alcanze_horizontal = self.x0 + ((self.velocidad_inicial*sin(2*self.angulo))/(2*self.gravedad)) + \
                             ((self.velocidad_inicial*cos(self.angulo)) /
                              (self.gravedad))*sqrt(((self.velocidad_inicial*sin(self.angulo))**2) + 2*self.y0*self.gravedad)
        x = linspace(0, alcanze_horizontal, 601)

        ecuacion_parametrica_x = (self.x0 + self.velocidad_inicial*cos(self.angulo)*x)
        ecuacion_parametrica_y = (self.y0 + self.velocidad_inicial*sin(self.angulo)*x-(self.gravedad/2)*x**2)
        self.actualizar_grafico(ecuacion_parametrica_x,ecuacion_parametrica_y)
        # Metodo para almacenar datos de las entradas de datos
        def copiar_valores(event):
            self.tiempo_datos[0] = entrada_tiempo.get()

            master.destroy()

        # Metodo para validar la entrada de datos (Solo Numeros por ahora)
        def check(v, p):
            if p.isdigit():
                return True
            elif p is "":
                return True
            else:
                return False
        # Datos Iniciales

        #  inicializa la ventana popup
        master = tk.Tk()
        master.title("Posicion")
        # Crea un frame contenedor para la izquierda y la derecha
        frame_arriba = ttk.Frame(master)
        frame_centro = ttk.Frame(master)
        frame_abajo = ttk.Frame(master)
        frame_aceptar = ttk.Frame(master)
        validacion_tiempo = (frame_abajo.register(check), '%v', '%P')
        #validacion_y = (frame_derecha.register(check), '%v', '%P')

        frame_arriba.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_centro.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_abajo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_aceptar.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Crea las titulos de la entrada de datos
        tiempo = ttk.Label(frame_abajo, text="Tiempo: ")
        aceptar = ttk.Button(frame_aceptar, text="ACEPTAR")
        tiempo_init = ttk.Label(frame_arriba, text="Intervalo de tiempo")
        tiempo_init_x = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init_y = ttk.Entry(frame_arriba, state='readonly')
        tiempo_init.pack(side=tk.TOP)
        tiempo_init_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_x.configure(state='normal')
        tiempo_init_x.delete(0,'end')
        tiempo_init_x.insert(0,"0")
        tiempo_init_x.configure(state='readonly')
        # inicializa el punto de interseccion del eje Y
        tiempo_init_y.configure(state='normal')
        tiempo_init_y.delete(0, 'end')
        tiempo_init_y.insert(0, "0")
        tiempo_init_y.configure(state='readonly')

        #Separador de datos
        separador = ttk.Separator(frame_centro, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)
        # Crea formularios para entrada de datos
        entrada_tiempo = ttk.Entry(frame_abajo, validate="key", validatecommand=validacion_tiempo)
        #entrada_y = ttk.Entry(frame_derecha, validate="key", validatecommand=validacion_y)

        tiempo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        #posicion_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        entrada_tiempo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
       # entrada_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        aceptar.pack(fill=tk.BOTH, expand=1)
        aceptar.bind("<Button-1>", copiar_valores)

    def boton_velocidadf(self):
        pass

    def boton_aceleracionf(self):
        #pop up de ingreso de datos

        #funcion para la obtencion de tiempo impacto final
        def time_impact(self):

            return 2.7

        Pop_Up = tk.Tk()
        Pop_Up.title("Aceleracion")
        Pop_Up.minsize(400,300)

        label = tk.Label(Pop_Up)
        label.pack()

        button = ttk.Button(Pop_Up, text = 'Evaluar' , width = 10, command = Pop_Up.destroy)
        button.pack(side=tk.BOTTOM)

        # funcion para el calculo de la coordenada horizontal
        def cord_x(self, t):
            x = self.x0 + ((self.velocidad_inicial * cos(self.angulo)) * t)
            return x

        # funcion para el calculo de la coordenada vertical
        def cord_y(self, t):
            y = self.y0 + (((self.velocidad_inicial * (cos(self.angulo))) * t) - ((self.gravedad / 2) * (t ** 2)))
            return y

        # generamiento de la grafica

        t = time_impact(self)
        time = np.arange(0,t,0.01)
        x = cord_x(self, time)
        y = cord_y(self, time)
        mpl.plot(x,y,"r--")
        mpl.show()

        #generacion del punto de posicion a medir


        #generacion del vector con origen en el punto de posicion


        #posible desplazamiento con deslizador
        pass

    def boton_alcance_horizontalf(self):
        pass

    def boton_altura_maximaf(self):
        pass

    def boton_camino_recorridof(self):
        pass

    def boton_radio_y_centro_de_curvatura_circulo_obsculadorf(self):
        pass

    def boton_aceleracion_normal_y_tangencialf(self):
        pass

    def boton_vector_normalf(self):
        pass
    def actualizar_grafico(self,ecuacion_x,ecuacion_y):
        self.figura.clear() # Refresca el gráfico
        self.figura.add_subplot(111).plot(ecuacion_x,ecuacion_y, "--")
        # self.figura.add_subplot(111).plot(x0, y0, 'r.')
        self.figura.canvas.draw()

    #
    # def actualizar_grafico(self):
    #     self.figura.clear() # Refresca el gráfico
    #     s = np.cos(2)
    #     self.figura.add_subplot(111).plot(self.ecuacion, self.ecuacion)
    #     self.figura.canvas.draw()

    # Lista de almacenado de datos
    tiempo_datos = [0, 0]