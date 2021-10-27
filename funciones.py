import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma

def limpiar(): #Esta funcion limpia la consola
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
