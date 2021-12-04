import funcion as F # Importa las funciones del archivo función.se apoda F.
import dibujo as D #Importa funciones de los dibujos.se apoda D.
import categoria as C #Importa categorías de las opciones.se apoda C
from random import choice as R #Importa la funcion para escoger una variable aleatoria de una lista.Se apoda R
from time import sleep #Importa una función para dormir al programa por un número de segundos. 
from json import load #Funcion que se utiliza para analizar una cadena JSON válida y convertirla en un diccionario de Python.
from operator import itemgetter as ITEM 

def opcion_1():
    '''
    -Trabaja con el módulo "dibujo o D" y con las función "Menu_El_Ahorcado" y la función "error".

    -Pide al usuario escoger cualquiera de las categorias disponibles.
  
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
  print("FALTAAAAA")

def opcion3():
    """
    -Trabaja con el módulo "dibujo".
    -Limpia la consola e imprime en pantalla "proximamente" y una pequeña animación.
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
        json_content = load(jsonfile) 

    nombres = sorted(json_content.items(), key=ITEM(1),  reverse=True) #Lista de tuplas
    
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


def UTEC_GAMES():
    '''
    -Trabaja con la función "menu_utec" del módulo "dibujo"
    -si la opción del menú es igual a 1 va a imprimir la función "introduccion" del módulo dibujo o D luego si ingresa la opción 2, 3, 4 o 5 va a ejecutar las funciones correspondientes y en caso ingrese otro caracter va a imprimirla función error del módulo "dibujo o D".

    '''
    Opcion_de_Menu = D.menu_utec()
    if Opcion_de_Menu == "1":
        D.introduccion()
        opcion_1()
    elif Opcion_de_Menu == "2":
        opcion2()
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
