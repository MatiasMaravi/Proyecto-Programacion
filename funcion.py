import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma
from random import choice as R  #Funcion para escoger una variable aleatoria de una lista
from time import sleep  #Funcion de aparicion del hilo de consola en un tiempo determinado
import categoria as C #listas de categorías de cada opción
import dibujo as D #funciones de los dibujos
import json 


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
    -Si encuentra coincidencias va a imprimir la letra y quitará el guión reemplazando por un espacio vacío.
    -Si la letra es vacío va a imprimir dos espacios.
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
    -Trabaja con el módulo "categoria"=C .
    -Trabaja con la función "choice"=R del módulo "random"que devuelve un valor aleatorio extraído de la secuencia categoría,consejos.
    -Imprime en pantalla un consejo aleatorio.
    """
    print("Consejo para tu vida:")
    print("------------------------\n")
    print(f"✩ {R(C.consejos)} ✩")
    print("\n")


def ganar(nombre,intentos):
    """
    -La función limpia la consola.
    -La función contiene los puntos según los errores: 0 errores igual a 60 puntos consecutivamente.
    -Imprime el nombre del ganador, junto con "GANASTE!!!".
    -La funcion imprime un mensaje de victoria y muestra al muñeco escapando del juego con el módulo dibujo = D, función salvado. 
    -Imprimirá el puntaje del jugador.
    -Por último imprimirá un consejo para tu vida con el módulo categoría, función consejos.
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
    -Imprimirá el mensaje ahorcado mediante el módulo "categoría", función ahorcadooo.
    -Imprimirá el mensaje de intentos agotados junto al nombre del jugador.
    -La funcion recibe como parámetro la palabra a adivinar que contiene el nombre de alguna palabra de la categoría y la muestra luego de imprimir un mensaje de derrota y mostrar al muñeco ahorcado completo. 
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
    -La función trabaja con tres parámetros, intentos que contiene el número de intentos que son 6. Errores, que contendrán los errores al ingresar mal la letra y categoría que contiene el nombre de la categoría escogida por el jugador.
    -La función limpia la consola
    -La función imprime el nombre "EL JUEGO DEL AHORCADO", e imprime la categoría escogida por el jugador. 
    -Imprime la función llamada "imprimir_ahorcado" dentro de módulo dibujo y trabaja con el parámetro "intentos"
    si la variable "intentos" es igual a 5 imprime un mensaje de precaución de que solo le queda 1 intento.Caso contrario imprimirá el número de errores menos el número de intentos totales.
    -Trabaja con el parámetro errores, con numero de errores en errores entonces imprimrá el numero de errores en una lista.
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
    -la función trabaja con dos parámetros:
    tu_letra:letra ingresada
    letras_ingresadas: lista de las letras que ingresaste
    -Lo que hace esta función es mostrar los mensaje de error dependiendo de las validaciones de las funciones.

    '''
    if letra_repetida(tu_letra, letras_ingresadas) == False:
        limpiar_consola()
        D.error(3)
        sleep(2.5)
        return False
        '''
        si tu letra es repetida con la lista de letras ingresadas limpia la consola, da un mensaje de error, espera 2.5 segundos y devuelve al interfas.

        '''

    elif len(tu_letra) > 1:
        limpiar_consola()
        D.error(4)
        sleep(2.5)
        return False
        '''
        si tu letra es mayor a 1 o sea si hay más de una letra, limpia la consola, da un mensaje de error, espera 2.5 segundos y devuelve al interfas.
        
        '''
    elif validar_letras_numeros(tu_letra) == False:
        limpiar_consola()
        D.error(5)
        sleep(2.5)
        return False
    
    else:
        return True
        '''
        si tu letra contiene un carácter especial que no sean letras o numeros, limpia la consola, da un mensaje de error, espera 2.5 segundos y devuelve al interfas.

        '''

def puntaje(nombre,intentos):
  
  '''
  -La función puntaje trabaja con dos parámetros: 
  nombre: nombre de los jugadores 
  intentos: numero de intentos
  -La función trabaja con un diccionario que contiene los puntajes por número de intentos.
  -Cuando se abra el archivo puntajes.json se apodará "archivo_json" que es la ruta se convertirá a python.
  '''
  puntos = {0:60, 1:50, 2:40, 3:30, 4:20, 5:10, 6:0}

  with open('puntajes.json','r') as archivo_json:
    puntos_jugadores = json.load(archivo_json)

  if nombre not in puntos_jugadores.keys():
    puntos_jugadores[nombre] = puntos[intentos]
    '''
    -Si el nombre del jugador no está en el archivo_json entonces se va a integrar al archivo json, y los puntos obtenidos por sus intentos.
    '''
  else:
    puntos_jugadores[nombre] += puntos[intentos]

  with open('puntajes.json','w') as archivo_json:
      json.dump(puntos_jugadores, archivo_json, indent=4) 
      '''
      -La función abrirá el "archivo_json" lo convertirá de python a jsn y lo cerrará con los datos actualizados.
      '''


def jugar(adivinar, categoria):
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
    
    nombre = input("Ingrese su nombre: ").upper()
    nombre.strip()
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
  


"""
Titulo

bla {sustantivo} bla bla bla bla bla bla bla bla bla bla bla bla bla
bla bla bla bla bla bla bla {lugar} bla bla bla bla bla bla bla
bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla
bla bla bla {numero} bla bla bla bla {comida} bla bla bla bla bla
bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla

"""


