import funcion as F
import dibujo as D
import categoria as C
from random import choice as R
from time import sleep
import json
 

def opcion1():
    """
  Trabaja con el módulo "dibujo" y con las función "Menu_El_Ahorcado" y 
  la función "error".
  Pide al usuario escoger cualquiera de las categorias disponibles.
  Si ingresas una opcion inválida se ejecutara nuevamente la función.
  """
    opcion = D.menu_ahorcado()
    if opcion == "1":
        F.limpiar_consola()
        nombre = D.a_jugar()
        F.jugar(R(C.peliculas_mas_vistas), "Peliculas Famosas",nombre)

    elif opcion == "2":
        F.limpiar_consola()
        nombre = D.a_jugar()
        F.jugar(R(C.videos_juegos), "Videojuegos",nombre)

    elif opcion == "3":
        F.limpiar_consola()
        nombre = D.a_jugar()
        F.jugar(R(C.frases_de_disney), "Frases de Disney",nombre)

    elif opcion == "4":
        F.limpiar_consola()
        nombre = D.a_jugar()
        F.jugar(R(C.deportes), "Deportes",nombre)

    elif opcion == "5":
        F.limpiar_consola()
        nombre = D.a_jugar()
        F.jugar(R(C.mujeres_historicas), "Mujeres Historicas",nombre)

    elif opcion == "6":
        F.limpiar_consola()
        nombre = D.a_jugar()
        F.jugar(R(C.refranes), "Refranes",nombre)
    elif opcion == "7":
        F.limpiar_consola()

    elif opcion == "REGLAS":
        F.limpiar_consola()
        D.reglas()
        opcion1()

    else:
        D.error(1)
        opcion1()


def opcion2():
  print("FALTAAAAA")

def opcion3():
    """
  Trabaja con el módulo "dibujo".
  Limpia la consola e imprime en pantalla "proximamente" y una pequeña animación.
  """
    F.limpiar_consola()
    print("Proximamente...\n")
    D.proximamente()
    sleep(2)
    F.limpiar_consola()

def opcion4():
    F.limpiar_consola()
    print("*** Clasificaciones***")
    with open('puntajes.json','r') as jsonfile:
        json_content = json.load(jsonfile) 
        jsonfile.close()
    nombres = F.ordenar_puntajes(json_content) #Lista de tuplas
    lugares = len(nombres)
    for i in range(1,lugares+1):
        print(f"{i}. {nombres[i-1][0]} ---> {nombres[i-1][1]} puntos ")
    input("Presione enter para regresar: ")


def opcion5():
    """
  Trabaja con el módulo "dibujo".
  Limpia la consola e imprime en pantalla un mensaje de despedida con un dibujo.
  """
    F.limpiar_consola()
    print("Adiós!!")
    D.despedida()




  