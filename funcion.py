import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma
from random import choice #Funcion para escoger una variable aleatoria de una lista
from time import sleep #Funcion de aparicion del hilo de consola en un tiempo determinado
import categoria
import dibujo

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
  lista_respaldo = [letra]
  for i in lista:
      if i  in lista_respaldo:
          return False     
      else:
          lista_respaldo.append(i)
  return True

def validar_especiales(pal):
  '''
  Esta función reconoce si el valor ingresado es una letra. Caso contrario retornara False.  
  '''
  for letra in pal:
      if letra not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
          return False
  return True

def Menu_UTEC_GAMES():
  """ 
  Trabaja con el módulo "dibujo".
  Esta Función mostrara el título del juego "UTEC GAMES" y un menú para que el usuario 
  seleccione la categoría o regrese al menú anterior. 
  Retorna la opcion ingresada.
  """
  dibujo.logo()
  print("Seleccione una categoría")
  print("1. Juego del ahorcado")
  print("2. Otros juegos")
  print("3. Salir \n")
  opcion = str(input("Ingrese una Opcion : "))
  return opcion

def Menu_El_Ahorcado():
    """
    Trabaja con el módulo "dibujo"
    Esta función limpia la consola y muestra el título del juego "El ahorcado", 
    además muestra un menú para que el usuario seleccione la categoría o regrese al menú anterior.
    Retorna la categoria escogida.
    """
    limpiar_consola()
    dibujo.logo()
    opc = str(input("Elige una categoría  \n\n"

                    "1. Peliculas Famosas \n" +
                    "2. Videojuegos \n" +
                    "3. Frases de Disney \n" +
                    "4. Deportes \n" +
                    "5. Mujeres Historicas \n" +
                    "6. Refranes  \n\n" +
                    "Elija una Opcion :D \n--→  "))
    return opc

def error(funcion):
  """
  Trabaja con el módulo "dibujo" y la función "sleep" del módulo "time".
  La funcion recibe otra funcion que ejecutara nuevamente pero antes limpiara 
  la consola y te avisara que habias cometido un error por unos segundos.
  """
  limpiar_consola()
  dibujo.error(1)
  print("")
  sleep(2)
  limpiar_consola()
  funcion()

def jugar(adivinar, categoria): 
  """
  Trabaja con el módulo "dibujo"

  Parámetros:
  adivinar -- palabra o frase que se utilizara para iterar.
  categoria -- Categoria a la que pertenece la palabra o frase a adivinar.
  Esta funcion recibe como parametro un string en mayusculas. Pedirá al usuario que
  ingresemos una letra y comenzará a iterar letra por letra buscando similitudes con las letras que vamos ingresando.
  
  -Si no encuentra letras coincidentes imprimira un guion bajo en su lugar.
  
  -La funcion muestra las letras erroneas

  -Solo permite ingresar una letra a la vez para comparar
  
  -Si ingresas una letra que no esta en la frase se contara como 
  un error

  -Si el parámetro a adivinar es una frase, el "espacio" no se
  considerara como un guion.

  -La funcion termina si al iterar no encuentra guiones bajos, entonces
  ganas el juego. 

  -Si pierdes tus 6 intentos tambien acaba la funcion y pierdes el juego

  -Puedes terminar el juego cuando desees si ingresas la palabra "SALIR"
  """
  adivinar = adivinar.upper() 
  intentos = 0
  errores = [] 
  letras_ingresadas = ""
  while True:
      if intentos < 6 :
        limpiar_consola()
        print("*** EL JUEGO DEL AHORCADO *** \n")
        print(f"Categoria: {categoria}")
        dibujo.imprimir_ahorcado(intentos)
        guiones = 0
        print("")

        if intentos == 5:
          print(f"CUIDADO!!! solo te queda {6-intentos} intento\n")
        else:
          print(f"Te quedan {6-intentos} intentos\n")
        print(f"Errores: ", end=" ")
        for error in errores:
           print(f"[ {error} ]",end=" ")
        print("\n")
        for letra in adivinar:
            if letra in letras_ingresadas: 
                print(letra,end=" ")
            elif letra == " ":
                print("  ",end=" ") 
            else:
                print("_",end=" ")
                guiones +=1

        print("")
        if guiones == 0: 
          limpiar_consola()
          print("")
          print("GANASTE!!!!", end="")
          dibujo.salvado()
          print("Completaste la frase, felicidades!!")
          sleep(2)
          limpiar_consola()
          break
        
        print("")
        tu_letra = input("Introduce tu letra: ").upper()
        if tu_letra == "SALIR":
          dibujo.muerte()
          break
        if letra_repetida(tu_letra, letras_ingresadas) == False:
          limpiar_consola()
          dibujo.error(3)
          sleep(2)
          
        elif len(tu_letra) >1:
          limpiar_consola()
          dibujo.error(4)
          sleep(1.5)
        
        elif validar_especiales(tu_letra) == False:
          limpiar_consola()
          dibujo.error(5)
          sleep(1.5)

        elif tu_letra not in adivinar:
            letras_ingresadas += tu_letra
            errores.append(tu_letra)
            limpiar_consola()
            intentos += 1

        else:
            limpiar_consola()
            letras_ingresadas += tu_letra

      else:
        dibujo.ahorcado()
        print("Intentos agotados, perdiste el juego")
        dibujo.imprimir_ahorcado(intentos)
        sleep(2)
        limpiar_consola()
        break

def volver_jugar(funcion):
  """
  Trabaja con el módulo "dibujo"
  Recibe como parámetro una funcion a ejecutar en caso el valor
  sea la palabra "SI"
  Esta funcion pregunta al usuario si quisiera volver a la
  sala principal o desea salir completamente del juego
  Si ingresa una opción inválida mostrara un dibujo de error
  """
  dibujo.volver()
  valor = input("(SI/NO) : ").upper()
  if valor == "SI":
    limpiar_consola()
    return funcion()
  elif valor == "NO":
    limpiar_consola()
    print("Adiós!!")
    dibujo.despedida()
  else:
    limpiar_consola()
    print("")
    dibujo.error(2)
    sleep(2)
    limpiar_consola()
    volver_jugar(funcion)

def opcion1():
  """
  Trabaja con el módulo "dibujo" y con las función "Menu_El_Ahorcado" y 
  la función "error".
  Pide al usuario escoger cualquiera de las categorias disponibles.
  Si ingress una opcion inválida se ejecutara nuevamente la función.
  """
  opcion = Menu_El_Ahorcado()
  if opcion == "1":
    limpiar_consola()
    dibujo.a_jugar()
    jugar(choice(categoria.peliculas_mas_vistas),"Peliculas Famosas")

  elif opcion == "2":
    limpiar_consola()
    dibujo.a_jugar()
    jugar(choice(categoria.videos_juegos),"Videojuegos")

  elif opcion == "3":
    limpiar_consola()
    dibujo.a_jugar()
    jugar(choice(categoria.frases_de_disney),"Frases de Disney")

  elif opcion == "4":
    limpiar_consola()
    dibujo.a_jugar()
    jugar(choice(categoria.deportes),"Deportes")

  elif opcion == "5":
    dibujo.a_jugar()
    jugar(choice(categoria.mujeres_historicas),"Mujeres Historicas")

  elif opcion == "6":
    limpiar_consola()
    dibujo.a_jugar()
    jugar(choice(categoria.refranes),"Refranes")

  else:
    limpiar_consola()
    error(opcion1)

def opcion2():
  """
  Trabaja con el módulo "dibujo".
  Limpia la consola e imprime en pantalla "proximamente" y una pequeña animación.
  """
  limpiar_consola()
  print("Proximamente...\n")
  dibujo.proximamente()
  sleep(2)
  limpiar_consola()

def opcion3():
  """
  Trabaja con el módulo "dibujo".
  Limpia la consola e imprime en pantalla un mensaje de despedida con un dibujo.
  """
  limpiar_consola()
  print("Adiós!!")
  dibujo.despedida()
  
def consejos():
  """
  Trabaja con el módulo "categoria".
  Trabaja con la función "choice" del módulo "random"
  Imprime en pantalla un consejo aleatorio.
  """
  print("Consejo para tu vida:\n")
  print(f"✩ {choice(categoria.consejos)} ✩")
  print("\n")
