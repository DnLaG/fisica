Física
======
[![Build Status](https://travis-ci.org/ofou/PhysicsUCM.svg?branch=master)](https://travis-ci.org/ofou/fisica)
[![Porcentaje de código aún por realizar](http://isitmaintained.com/badge/open/ofou/physicsucm.svg)](https://github.com/ofou/fisica/issues "Percentage of issues still open")
[![Tiempo promedio para terminar una tarea](http://isitmaintained.com/badge/resolution/ofou/physicsucm.svg)](https://github.com/ofou/fisica/issues?q=is%3Aissue+is%3Aclosed "Average time to resolve an issue")
![GitHub contributors](https://img.shields.io/github/contributors/ofou/fisica.svg)

Herramientas de visualización para ayudar al estudio Fisica Universitaria. 

![good motion ah?](http://i407.photobucket.com/albums/pp152/miniman796/Pivot/BasketballShot.gif)

Información general
-------------------

El presente proyecto tiene como fin crear una serie de visualizaciones y módulos interactivos de ejercicios de cinemática, especificamente de [movimiento parabólico](https://es.wikipedia.org/wiki/Movimiento_parab%C3%B3lico), más conocido como movimiento proyectil. El prof. Hugo Ibañez nos entregó unas diapositivas a modo de [inspiración](https://github.com/ofou/fisica/raw/master/docs/PROYECTO%20SOFTWARE%20PROYECTIL%20-%20PRESENTACION%20-%20HUGO.ppsx) sobre lo que debería contener el proyecto. Pero finalmente el software final será diseñado y programado por nosotros, así que todas las ideas originales son bienvenidas. Algunas de las funciones principales del software será la capacidad de manipular datos sobre las ecuaciones de trayectoria parabólica, visualizar el movimiento balístico, entre [otras](https://github.com/ofou/fisica/issues) funciones interesantes.

Como para muchos este es su primer encuentro con el software colaborativo de código libre, vamos a detallar muy claramente todo el proceso y la información necesaria para colaborar. Si tienen alguna duda sobre _lo que sea_, no duden en [abrir un issue](https://github.com/ofou/fisica/issues/new) para que la comunidad pueda resolver sus interrogantes. Si tienen dudas, también pueden consultar directamente a los directores del proyecto utilizando @ofou (Omar Olivares) o @Owllxz (Luis Sepúlveda). La idea es que esta sea una experiencia enriquecedora para todos y que mejor que hacerlo open source. 

Dentro de los detalles técnicos, para el presente trabajo utilizaremos [Git](https://git-scm.com/downloads) + [Github](https://github.com/join) para el trabajo colaborativo. El lenguaje de programación escogido fue Python el cual es el lenguaje en común, ahora para evitar problemas **todos** deben instalar y utilizar Python en su [**Versión 3.7**](https://www.python.org/downloads/release/python-370/) ya que será la versión oficial de este proyecto. Si deciden utilizar otra versión, y sus códigos no son compatibles con el código fuente, serán rechazados sus aportes al proyecto hasta no corregir los errores. También hemos escogido [Tkinter](https://docs.python.org/3.7/library/tk.html) como la librería gráfica para el proyecto dado a su extensa documentación y amplio número de tutoriales en internet, además de tener la ventaja de ser una librería incorporada en Python. Para este proyecto en especial, recomendamos el uso de un IDE especializado, especificamente [Pycharm](https://www.jetbrains.com/pycharm/) dado a que les ayudará a corregir errores menores, mantener un formato adecuado y además de tener la ventaja de tener un sistema de control de versiones integrado. 

> "Para los que no tengan mucha experiencia utilizando versiones de control realicé [un pequeño screencast](https://youtu.be/DKuHYdk4LAg) de la instalación en Windows y un tutorial breve de cómo colaborar a través de Github." – Omar

Instalación
------------
#### Linux (>=Ubuntu 16.04)
```bash
sudo apt-get install git
sudo apt-get install python3.7
sudo snap install pycharm-community
```

#### OSX
* Descargar e instalar [Git](https://git-scm.com/downloads), [Python 3.7](https://www.python.org/downloads/release/python-370/) y [Pycharm](https://www.jetbrains.com/pycharm/) (opcional)

#### Windows
* Descargar e instalar [Git](https://git-scm.com/downloads), [Python 3.7](https://www.python.org/downloads/release/python-370/) y [Pycharm](https://www.jetbrains.com/pycharm/) (opcional)

Cómo colaborar
--------------
0. Hacer un [Fork](https://guides.github.com/activities/forking/) del repositorio central
1. Clonar (localmente) el Fork que acabas de crear. `git clone https://github.com/USERNAME/fisica.git`
2. Configurar el repositorio original con el personal usando `git remote add upstream https://github.com/ofou/fisica.git` (Es necesario solo la primera vez)
2. Añadir los archivos con cambios `git add ejemplo.txt` o añadir todos (con precaución) `git add .`
3. Realizar un commit con una breve descripción de los cambios `git commit -m "Breve descripción"`
4. Hacer un `pull request` para enviar los cambios al repositorio central
5. Para mantener [actualizado](https://www.youtube.com/watch?v=o-2fvj7GsOQ) tu repositorio con el repositorio central `git pull upstream master` o `git fetch` si ya tienes configurado los remotes

Roadmap
-------
- [x] Detalles del proyecto
- [x] Instrucciones de instalación
- [x] Creación de tutoriales
- [ ] Asignación de tareas
- [ ] Desarrollo

Recomendaciones
---------------
* Es imprecindible que **documenten bien** su código, para facilitar la comprensión y trabajo en equipo. Habrá información adicional en la wiki del proyecto que pueden visitar para tener una idea de como documentar bien el código fuente.
* Siempre reciban los cambios del repositorio antes de enviar los suyos, para evitar problemas.

