import matplotlib.pyplot as plt
import math

def seno(Grado):
 #funcion para calcualar el seno de un angulo
 #transforma el angulo a radianes para la funcion sin
	return math.sin(math.radians(Grado))
def coseno(Grado):
	#funcion para calcualar el seno de un angulo
	#transforma el angulo a radianes para la funcion sin
	return math.cos(math.radians(Grado))

def Ingreso_De_Datos():
	#funcion que recibe y retorna los valores para reemplazar en la ecuacion.
	V_inicial=int(input("Velocidad inicial: "))
	Angulo=int(input("Angulo de inclinación:"))
	Aceleracion=int(input("Aceleracion: "))
	Tiempo=int(input("Tiempo: "))
	#retorn de los datos leidos  por teclado.
	return V_inicial,Angulo,Aceleracion,Tiempo

def Vector_Velocidad(v0,O,a,t):
	#funcion que calcula el vector velocidad
	#como parametro recibe los valores de velocidad,angulo,aceleracion y tiempo.
	Vt = []
	Vx = v0*(coseno(O))
	Vy = v0*(seno(O))-a*t
	#se añaden la velocidad en X e Y al vector Vt.
	Vt.append(Vx)
	Vt.append(Vy)
	return Vt

def Grafica_Velocidad(Vt):
	#funcion para graficar el vector velocidad.
	plt.plot(Vt,"r-")
	plt.show()

def Mostrar_Vector(Vt):
	#muestra el vector velocidad por consola.
	print(Vt[0],",",Vt[1])

if __name__=="__main__":
	V_Inicial,Angulo,Aceleracion,Tiempo = Ingreso_De_Datos()
	Velocidad = Vector_Velocidad(V_Inicial,Angulo,Aceleracion,Tiempo)
	Mostrar_Vector(Velocidad)
	Grafica_Velocidad(Velocidad)