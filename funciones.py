import os #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma

def limpiar():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

