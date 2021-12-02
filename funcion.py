import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma
from random import choice as R  #Funcion para escoger una variable aleatoria de una lista
from time import sleep  #Funcion de aparicion del hilo de consola en un tiempo determinado
import categoria as C
import dibujo as D
import json



def limpiar_consola():
    """
  Trabaja con los módulos "platform" y "os" 
  Esta funcion limpia la consola dependiendo 
  que sistema operativo estes usando
  """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def letra_repetida(letra, lista):
    """
  Parametros:
  letra -- valor que vas a ver si se repite en una lista
  lista -- lista de valores 

  La funcion compara si la variable que ingresamos se encuentra
  en la lista y retorna "False" de ser el caso.
  En caso la letra no se encuentre en la lista retorna "True"
  """
    for i in lista:
        if letra == i:
            return False
    return True


def validar_especiales(pal):
    '''
  Esta función reconoce si el valor ingresado es una letra. Caso contrario retornara False.  
  '''
    for letra in pal:
        if letra not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789":
            return False
    return True


def imprimir_guiones(adivinar, letras_ingresadas):
    """
    -Si no encuentra letras coincidentes imprimira un guion bajo en su lugar.

    -Si el parámetro a adivinar es una frase, el "espacio" no se considerara como un guion.
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
  Trabaja con el módulo "categoria".
  Trabaja con la función "choice" del módulo "random"
  Imprime en pantalla un consejo aleatorio.
  """
    print("Consejo para tu vida:")
    print("------------------------\n")
    print(f"✩ {R(C.consejos)} ✩")
    print("\n")


def ganar(nombre):
    """
    La funcion imprime un mensaje de victoria y muestra al muñeco
    escapando del juego. 
    Pedira al usuario que ingrese alguna tecla para continuar
    """
    limpiar_consola()
    print("")
    print(f"{nombre} GANASTE!!!", end="")
    D.salvado()
    print("Completaste la frase, felicidades!!!\n")
    consejos()
    input("Ingresa cualquier tecla para continuar: ")
    limpiar_consola()

def perder(adivinar,nombre):
    """
    La funcion recibe como parametro la palabra a adivinar y la muestra luego
    de imprimir un mensaje de derrota y mostrar al muñeco
    ahorcado. 
    Pedira al usuario que ingrese alguna tecla para continuar
    """
    D.ahorcadooo()
    print(f"Intentos agotados, perdiste el juego {nombre}\n")
    print(f"La palabra era '{adivinar}'")
    D.imprimir_ahorcado(6)
    input("\nIngresa cualquier tecla para continuar: ")
    limpiar_consola()


def interfaz(intentos, errores, categoria):
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
    for error in errores:
        print(f"[ {error} ]", end=" ")
    print("\n")


def validacion_de_reglas(tu_letra, letras_ingresadas):
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

    elif validar_especiales(tu_letra) == False:
        limpiar_consola()
        D.error(5)
        sleep(2.5)
        return False
    else:
        return True

def puntaje(nombre,intentos):

  puntos = {0:60, 1:50, 2:40, 3:30, 4:20, 5:10, 6:0}

  with open('puntajes.json','r') as archivo_json:
    jugadores_puntos = json.load(archivo_json)

  if nombre not in jugadores_puntos.keys():
    jugadores_puntos[nombre] = puntos[intentos]

  else:
    jugadores_puntos[nombre] += puntos[intentos]

  with open('puntajes.json','w') as archivo_json:
      json.dump(jugadores_puntos, archivo_json, indent=4) 


def jugar(adivinar, categoria,nombre):
    """
  Trabaja con el módulo "dibujo"

  Parámetros:
  adivinar -- palabra o frase que se utilizara para iterar.
  categoria -- Categoria a la que pertenece la palabra o frase a adivinar.
  Esta funcion Pedirá al usuario que ingresemos una letra y comenzará a iterar letra por letra buscando similitudes con las letras que vamos ingresando.
  
  -La funcion muestra las letras erroneas

  -Si ingresas una letra que no esta en la frase se contara como un error

  -La funcion termina si al iterar no encuentra guiones bajos, entonces ganas el juego. 

  -Si pierdes tus 6 intentos tambien acaba la funcion y pierdes el juego

  -Puedes terminar el juego cuando desees si ingresas la palabra "SALIR"
  """
    adivinar = adivinar.upper()
    intentos = 0
    errores = []
    letras_ingresadas = ""
    while intentos < 6:

        interfaz(intentos, errores, categoria)
        guiones = imprimir_guiones(adivinar, letras_ingresadas)

        if guiones == 0:
            puntaje(nombre,intentos)
            return ganar(nombre)

        tu_letra = input("\nIntroduce tu letra: ").upper()
        if tu_letra == "SALIR":
            return D.muerte()

        elif validacion_de_reglas(tu_letra, letras_ingresadas):

            if tu_letra not in adivinar:
                letras_ingresadas += tu_letra
                errores.append(tu_letra)
                limpiar_consola()
                intentos += 1

            else:
                limpiar_consola()
                letras_ingresadas += tu_letra
    puntaje(nombre,intentos)
    return perder(adivinar,nombre)


def volver_sala(funcion):
    """
  Trabaja con el módulo "dibujo"
  Recibe como parámetro una funcion a ejecutar en caso el valor
  sea la palabra "SI"
  Esta funcion pregunta al usuario si quisiera volver a la
  sala principal o desea salir completamente del juego
  Si ingresa una opción inválida mostrara un dibujo de error
  """
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
  

import operator
def ordenar_puntajes(puntajes):
  return sorted(puntajes.items(), key=operator.itemgetter(1),  reverse=True)



"""
Titulo

bla {sustantivo} bla bla bla bla bla bla bla bla bla bla bla bla bla
bla bla bla bla bla bla bla {lugar} bla bla bla bla bla bla bla
bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla
bla bla bla {numero} bla bla bla bla {comida} bla bla bla bla bla
bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla

"""


