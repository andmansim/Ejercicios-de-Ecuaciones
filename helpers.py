import os
import re #para comprobar si lo que nos dan está bien
import platform #detecta el sistema operativo que queremos y lo adapta para poder trabajar con él.

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')