import funcion as F # Importa las funciones del archivo función. Se apoda F.
import dibujo as D #Importa funciones de los dibujos. Se apoda D.
import categoria as C #Importa categorías de las opciones. Se apoda C.
from random import choice as R #Importa la funcion para escoger una variable aleatoria de una lista. Se apoda R.
from time import sleep #Importa una función para dormir al programa por un número de segundos. 
from json import load #Funcion que se utiliza para analizar una cadena JSON válida y convertirla en un diccionario de Python.
from operator import itemgetter   #Importa la función para asignar indices en una lista, tupla o diccionario.

import historias as H #Importa las fuciones del archivo historias. Se apoda H.

def opcion_1():
    '''
    Presenta las funcionalidades del Juego del Ahorcado.

    -Trabaja con el módulo "dibujo o D" y con las función "Menu_El_Ahorcado" y la función "error".

    -Esta función pide al usuario escoger cualquiera de las categorias disponibles.
  
    -Si ingresas una opcion inválida se ejecutara nuevamente la función.
    '''
    opcion = D.menu_ahorcado()
    if opcion == "1":
        F.limpiar_consola()
        F.jugar(R(C.peliculas_mas_vistas), "Peliculas Famosas")
        F.volver_sala(UTEC_GAMES)
    elif opcion == "2":
        F.limpiar_consola()
        F.jugar(R(C.videos_juegos), "Videojuegos")
        F.volver_sala(UTEC_GAMES)
    elif opcion == "3":
        F.limpiar_consola()
        F.jugar(R(C.frases_de_disney), "Frases de Disney")
        F.volver_sala(UTEC_GAMES)
    elif opcion == "4":
        F.limpiar_consola()
        F.jugar(R(C.deportes), "Deportes")
        F.volver_sala(UTEC_GAMES)
    elif opcion == "5":
        F.limpiar_consola()
        F.jugar(R(C.mujeres_historicas), "Mujeres Historicas")
        F.volver_sala(UTEC_GAMES)
    elif opcion == "6":
        F.limpiar_consola()
        F.jugar(R(C.refranes), "Refranes")
        F.volver_sala(UTEC_GAMES)
    elif opcion == "7":
        F.limpiar_consola()
        UTEC_GAMES()

    elif opcion == "REGLAS":
        F.limpiar_consola()
        D.reglas()
        opcion_1()

    else:
        D.error(1)
        opcion_1()

def opcion2():
  """
  Presenta las funcionalidades del Juego de Mad Story
  
  -Trabaja con los módulos "dibujo o D" y "hola".

  -En el módulo "historias o H" pide al usuario que introduzca los datos correspondientes y que estos reemplazarán a los términos de la historia seleccionada en diccionario "valores".

  { aun falta contenido }
  """
  historia = R(C.historias)
  if historia == "historias/historia1.txt":
    F.limpiar_consola()
    valores = H.historia1()
    H.reemplazar(historia, valores)
  elif historia == "historias/historia2.txt":
    F.limpiar_consola()
    valores = H.historia2()
    H.reemplazar(historia, valores)
  elif historia == "historias/historia3.txt":
    F.limpiar_consola()
    valores = H.historia3()
    H.reemplazar(historia, valores)
  elif historia == "historias/historia4.txt":
    F.limpiar_consola()
    valores = H.historia4()
    H.reemplazar(historia, valores)
  elif historia == "historias/historia5.txt":
    F.limpiar_consola()
    valores = H.historia5()
    H.reemplazar(historia, valores)

def opcion3():
    """
    -Trabaja con el módulo "dibujo o D".

    -Esta función limpia la consola e imprime en pantalla "proximamente" y una pequeña animación.
  """
    F.limpiar_consola()
    print("Proximamente...\n")
    D.proximamente()
    sleep(2)
    F.limpiar_consola()

def opcion4():
    """
    -Trabaja con el módulo "funcion o F"
    
    -Esta función limpia la consola y muestra los puntajes recopilados de cada usuario en una lista de clasificaciones leidos del archivo "puntajes.json" actualizado.

    -Pedirá al usuario que presione Enter para salir y se limpiará la consola.
    """
    F.limpiar_consola()
    print("*** Clasificaciones***\n")
    with open('puntajes.json','r') as jsonfile:
        json_content = load(jsonfile) 

    nombres = sorted(json_content.items(), key=itemgetter(1),  reverse=True) #Lista de tuplas
    
    lugares = len(nombres)
    for i in range(1,lugares+1):
        print(f"{i}. {nombres[i-1][0]} ---> {nombres[i-1][1]} puntos ")

    input("\nPresione enter para regresar: ")


def opcion5():
    """
  Trabaja con el módulo "dibujo o D".
  Esta función Limpia la consola e imprime en pantalla un mensaje de despedida con un dibujo.
  """
    F.limpiar_consola()
    print("Adiós!!")
    D.despedida()


def UTEC_GAMES():
    '''
    -Trabaja con la función "menu_utec" del módulo "dibujo"
    
    -Es la primera función en ejecutar el programa y nos presentan los juegos de "UTEC GAMES".

    -Esta función valida a través de distintas opciones. Si la opción del menú es 1 imprime las funciones del "Juego del ahorcado" y si ingresara la opción 2 imprime las funciones del "Mad Story".
    
    -Las opciones 3, 4 o 5 va a ejecutar las funciones correspondientes que no son juegos y en caso ingrese otro caracter va a imprimir un error.

    '''
    Opcion_de_Menu = D.menu_utec()
    if Opcion_de_Menu == "1":
        D.introduccion()
        opcion_1()
    elif Opcion_de_Menu == "2":
        D.introduccion_madstory()
        opcion2()
        F.volver_sala(UTEC_GAMES)
    elif Opcion_de_Menu == "3":
        opcion3()
        UTEC_GAMES()
    elif Opcion_de_Menu == "4":
        opcion4()
        UTEC_GAMES()
    elif Opcion_de_Menu == "5":
        opcion5()
    else:
        D.error(1)
        UTEC_GAMES()


if __name__ == "__main__":
  UTEC_GAMES()
