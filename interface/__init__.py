# El presente archivo tiene el proposito de reconocer la carpeta que lo contiene como un package externo y cada uno
# de los archivos como modulos que pueden ser importados

from interface import ideal
from interface import balistica
from interface import admin

__all__ = ['ideal', 'balistica', 'admin']