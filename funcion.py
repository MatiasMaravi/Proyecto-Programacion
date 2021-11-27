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

def Menu_UTEC_GAMES():
  """ 
  Trabaja con el módulo "dibujo".
  Esta Función mostrara el título del juego "UTEC GAMES" y un menú para que el usuario 
  seleccione la categoría o regrese al menú anterior. 
  Retorna la opcion ingresada.
  """
  dibujo.logo()

  opcion = str(input("Ingrese una Opcion --→ "))
  return opcion

def Menu_El_Ahorcado():
    """
    Trabaja con el módulo "dibujo"
    Esta función limpia la consola y muestra el título del juego "El ahorcado", 
    además muestra un menú para que el usuario seleccione la categoría o regrese al menú anterior.
    Retorna la categoria escogida.
    """
    limpiar_consola()
    dibujo.logo_ahorcado()

    opc = str(input( "Elija una Opcion :D --→ ")).upper() 
    return opc


def error(funcion):
  """
  Trabaja con el módulo "dibujo" y la función "sleep" del módulo "time".
  La funcion recibe otra funcion que ejecutara nuevamente pero antes limpiara la consola y te avisara que habias cometido un error por unos segundos.
  """
  limpiar_consola()
  dibujo.error(1)
  print("")
  sleep(2)
  limpiar_consola()
  funcion()

def imprimir_guiones(adivinar,letras_ingresadas):
    """
    -Si no encuentra letras coincidentes imprimira un guion bajo en su lugar.

    -Si el parámetro a adivinar es una frase, el "espacio" no se considerara como un guion.
    """
    guiones = 0
    for letra in adivinar:
      if letra in letras_ingresadas: 
          print(letra,end=" ")
      elif letra == " ":
          print("  ",end=" ") 
      else:
          print("_",end=" ")
          guiones +=1
    print("")
    return guiones

def perder(adivinar):
    """
    La funcion recibe como parametro la palabra a adivinar y la muestra luego
    de imprimir un mensaje de derrota y mostrar al muñeco
    ahorcado. 
    Pedira al usuario que ingrese alguna tecla para continuar
    """
    dibujo.ahorcadooo()
    print("Intentos agotados, perdiste el juego\n")
    print(f"La palabra era '{adivinar}'")
    dibujo.imprimir_ahorcado(6)
    input("\nIngresa cualquier tecla para continuar: ")
    limpiar_consola()

def consejos():
  """
  Trabaja con el módulo "categoria".
  Trabaja con la función "choice" del módulo "random"
  Imprime en pantalla un consejo aleatorio.
  """
  print("Consejo para tu vida:")
  print("------------------------\n")
  print(f"✩ {choice(categoria.consejos)} ✩")
  print("\n")

def ganar():
    """
    La funcion imprime un mensaje de victoria y muestra al muñeco
    escapando del juego. 
    Pedira al usuario que ingrese alguna tecla para continuar
    """
    limpiar_consola()
    print("")
    print("GANASTE!!!", end="")
    dibujo.salvado()
    print("Completaste la frase, felicidades!!\n")
    consejos()
    input("Ingresa cualquier tecla para continuar: ")
    limpiar_consola()  

def interfaz(intentos,errores,categoria):
      limpiar_consola()
      print("*** EL JUEGO DEL AHORCADO *** \n")
      print(f"Categoria: {categoria}")
      dibujo.imprimir_ahorcado(intentos)
      print("")
      if intentos == 5:
        print(f"CUIDADO!!! solo te queda 1 intento\n")
      else:
        print(f"Te quedan {6-intentos} intentos\n")
        
      print(f"Errores: ", end=" ")
      for error in errores:
          print(f"[ {error} ]",end=" ")
      print("\n")

def validacion_de_reglas(tu_letra,letras_ingresadas):
    if letra_repetida(tu_letra, letras_ingresadas) == False:
      limpiar_consola()
      dibujo.error(3)
      sleep(2.5)
      return False

    elif len(tu_letra) >1:
      limpiar_consola()
      dibujo.error(4)
      sleep(2.5)
      return False
  
    elif validar_especiales(tu_letra) == False:
      limpiar_consola()
      dibujo.error(5)
      sleep(2.5)
      return False
    else:
      return True

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
  while intentos < 6:
    interfaz(intentos,errores,categoria)
    guiones = imprimir_guiones(adivinar,letras_ingresadas)
    
    if guiones == 0: 
      return ganar()

    print()
    tu_letra = input("Introduce tu letra: ").upper()
    if tu_letra == "SALIR":
      return dibujo.muerte()

    if validacion_de_reglas(tu_letra,letras_ingresadas):
      
      if tu_letra not in adivinar:
          letras_ingresadas += tu_letra
          errores.append(tu_letra)
          limpiar_consola()
          intentos += 1

      else:
          limpiar_consola()
          letras_ingresadas += tu_letra

  return perder(adivinar)


def volver_sala(funcion):
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
    volver_sala(funcion)

def opcion1():
  """
  Trabaja con el módulo "dibujo" y con las función "Menu_El_Ahorcado" y 
  la función "error".
  Pide al usuario escoger cualquiera de las categorias disponibles.
  Si ingresas una opcion inválida se ejecutara nuevamente la función.
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
  elif opcion == "REGLAS":
    limpiar_consola()
    dibujo.reglas()
    opcion1()    

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