import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma
from random import choice as R  #Funcion para escoger una variable aleatoria de una lista
from time import sleep  #Funcion de aparicion del hilo de consola en un tiempo determinado
import categoria as C #listas de categorías de cada opción
import dibujo as D #Funciones de los dibujos
import json #Importa la funcion del manejo de archivos json en Python.


def limpiar_consola():
    """
    -Trabaja con los módulos "platform" y "os"

    -Esta funcion limpia la consola dependiendo que sistema operativo estes usando
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def letra_repetida(letra, lista):
    """
    Parametros:

    -letra --> valor que vas a ver si se repite en una lista

    -lista --> lista de valores 

    -La funcion compara si la letra que ingresamos se encuentra en la lista y retorna "False" de ser el caso.
    -En caso la letra no se encuentre en la lista retorna "True"
    """
    for i in lista:
        if letra == i:
            return False
    return True


def validar_letras_numeros(lista):
    '''
    Parámetros:

    -lista --> lista de valores

    -Esta función examina que letra se encuentre en la lista.

    -Esta función reconoce si el valor ingresado es una letra o número. Caso contrario retornara False.  
    '''
    for letra in lista:
        if letra not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789":
            return False
    return True


def imprimir_guiones(adivinar, letras_ingresadas):
    """
    Parámetros: 

    -adivinar --> string de la palabra a adivinar.
    letras_ingresadas --> string con todas las letras ingresadas por el usuario.

    -Esta función imprime los guiones y busca coincidencias  e imprime las letras_ingresadas quitando los guiones.
    """
    guiones = 0
    for letra in adivinar:
        if letra in letras_ingresadas:
            print(letra, end=" ")
        elif letra == " ":
            print("  ", end=" ")
        else:
            print("_", end=" ")
            guiones += 1
    print("")
    return guiones


def consejos():
    """
    Esta función imprime un consejo aleatorio para tu vida y trabaja con el módulo categorías.
    """
    print("Consejo para tu vida:")
    print("------------------------\n")
    print(f"✩ {R(C.consejos)} ✩")
    print("\n")


def ganar(nombre,intentos):
    """
    Parámetros: 

    -nombre --> se almacena el nombre del jugador

    -intentos --> se almacena el número de errores

    -La funcion imprime un mensaje de victoria y el nombre del juegador cuando gana, luego su puntaje de acuerdo al número de errores y además muestra al muñeco escapando del juego y finalmente un consejo para tu vida.

    -Pedira al usuario que ingrese alguna tecla para continuar y limpiará la consola.
    """
    puntos = {0:60, 1:50, 2:40, 3:30, 4:20, 5:10, 6:0}
    limpiar_consola()
    print("")
    print(f"{nombre} GANASTE!!!", end="")
    D.salvado()
    print("Completaste la frase, felicidades!!!")
    print(f"Tu puntaje fue de {puntos[intentos]} puntos\n")
    consejos()
    input("Ingresa cualquier tecla para continuar: ")
    limpiar_consola()


def perder(adivinar,nombre):
    """
    Parámetros: 

    -adivinar --> contiene el nombre de la categoría elegida.

    -nombre--> contiene el nombre del jugador.
    
    -La función imprime el mensaje "ahorcadoo" cuando no tengamos ningún intento más luego el muñeco ahorcado por completo. 

    -Pedira al usuario que ingrese alguna tecla para continuar
    """
    D.ahorcadooo()
    print(f"Intentos agotados, perdiste el juego {nombre}\n")
    print(f"La palabra era '{adivinar}'")
    D.imprimir_ahorcado(6)
    input("\nIngresa cualquier tecla para continuar: ")
    limpiar_consola()


def interfaz(intentos, errores, categoria):
    '''
    Parámetros:

    -intentos --> contiene el número de intentos
    errores --> contiene el numero de errores al ingresar mal la letra.

    -Categoria --> contiene el nombre de la categoría escogida por el jugador

    -La función imprime el nombre "EL JUEGO DEL AHORCADO",la categoría escogida por el jugador,los intentos y errores. Además pide al usuario introducir una letra para jugar. 
    '''
    limpiar_consola()
    print("*** EL JUEGO DEL AHORCADO *** \n")
    print(f"Categoria: {categoria}")
    D.imprimir_ahorcado(intentos)
    print("")
    if intentos == 5:
        print(f"CUIDADO!!! solo te queda 1 intento\n")
    else:
        print(f"Te quedan {6-intentos} intentos\n")
    print(f"Errores: ", end=" ")
  
    for numero_errores in errores:
        print(f"[ {numero_errores} ]", end=" ")
    print("\n")


def validacion_de_reglas(tu_letra, letras_ingresadas):
    '''
    Parámetros: 

    -tu_letra --> contiene la letra ingresada
    
    -letras_ingresadas --> lista de las letras que ingresaste
    
    -Lo que hace esta función es mostrar los mensaje de error dependiendo de las validaciones de las funciones.

    '''
    if letra_repetida(tu_letra, letras_ingresadas) == False:
        limpiar_consola()
        D.error(3)
        sleep(2.5)
        return False

    elif len(tu_letra) > 1:
        limpiar_consola()
        D.error(4)
        sleep(2.5)
        return False

    elif validar_letras_numeros(tu_letra) == False:
        limpiar_consola()
        D.error(5)
        sleep(2.5)
        return False
    
    else:
        return True


def puntaje(nombre,intentos):
  '''
  Parámetros: 

  -nombre -->  contien el nombre de los jugadores 
  
  -intentos--> contiene el número de intentos

  -La función abre un arhivo llamado "puntajes.json" que se apodará "archivo_json" y si el nombre del jugador no está en el "archivo_json" entonces se va a integrar al archivo json, y los puntos obtenidos por sus intentos.

  -La función abrirá el "archivo_json" lo convertirá de python a json y lo cerrará con los datos actualizados.
  '''
  puntos = {0:60, 1:50, 2:40, 3:30, 4:20, 5:10, 6:0}

  with open('aqui_git_hub/Proyecto-Programacion/puntajes.json','r') as archivo_json:
    puntos_jugadores = json.load(archivo_json)

  if nombre not in puntos_jugadores.keys():
    puntos_jugadores[nombre] = puntos[intentos]
  else:
    puntos_jugadores[nombre] += puntos[intentos]
  with open('aqui_git_hub/Proyecto-Programacion/puntajes.json','w') as archivo_json:
      json.dump(puntos_jugadores, archivo_json, indent=4) 


def jugar(adivinar, categoria):
    """
  Trabaja con el módulo "dibujo"

  Parámetros:

  -adivinar --> palabra o frase que se utilizara para iterar.

  -categoria --> Categoria a la que pertenece la palabra o frase a adivinar.

  -Esta funcion Pedirá al usuario que ingresemos una letra y comenzará a iterar letra por letra buscando similitudes con las letras que vamos ingresando mostrando los errores, termina cuando al iterar no encuentra guiones bajos también cuando pierdes tus 6 intentos.

  -Puedes terminar el juego cuando desees si ingresas la palabra "SALIR"
  """
    adivinar = adivinar.upper()
    intentos = 0
    errores = []
    letras_ingresadas = ""
    nombre = D.pedir_nombre().upper()
    nombre = nombre.replace(" ","")
    while intentos < 6:

        interfaz(intentos, errores, categoria)
        guiones = imprimir_guiones(adivinar, letras_ingresadas)

        if guiones == 0:
            puntaje(nombre,intentos)
            return ganar(nombre,intentos)

        tu_letra = input("\nIntroduce tu letra: ").upper()
        if tu_letra == "SALIR":
            return D.muerte()

        elif validacion_de_reglas(tu_letra, letras_ingresadas):
            letras_ingresadas += tu_letra
            if tu_letra not in adivinar:
                errores.append(tu_letra)
                intentos += 1

    puntaje(nombre,intentos)
    return perder(adivinar,nombre)


def volver_sala(funcion):
    """
    Parámetro:

    -funcion --> función a ejecutar
    
    -Trabaja con el módulo "dibujo"

    -Esta funcion pregunta al usuario si quisiera volver a la sala principal o desea salir completamente del juego y si ingresa una opción inválida mostrara un dibujo de error.
    """
    limpiar_consola()
    D.volver()
    valor = input("(SI/NO) : ").upper()
    if valor == "SI":
        limpiar_consola()
        return funcion()
    elif valor == "NO":
        limpiar_consola()
        print("Adiós!!")
        D.despedida()
    else:
        limpiar_consola()
        print("")
        D.error(2)
        sleep(2)
        limpiar_consola()
        volver_sala(funcion)
