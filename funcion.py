import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma
from random import choice #Funcion para escoger una variable aleatoria de una lista
from time import sleep #Funcion para la aparicion de la consola en un tiempo determinado
import categoria
import dibujo
#cosas por mejorar y agregar:

def limpiar_consola(): 
  """
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
  Esta función reconoce palabras mayusculas y minusculas menos carácteres especiales ni numeros.
  lo que hace este código es definir los parámetros pal que devuelve False mediante return en caso haya detectado la sentencia if una de las letras que no esten definidas en la variable letra, y si no es el caso retorna True y mediante el bucle for vuelve a repetirse la función.  
  '''
  for letra in pal:
      if letra not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz":
          return False
  return True

def Menu_UTEC_GAMES():
  """ Esta Función mostrara el título del juego "UTEC GAMES" y un menú para que el usuario seleccione la categoría o regrese al menú anterior 
  """
  print(" ***UTEC GAMES***\n")
  print("Seleccione una categoría")
  print("[1] Juego del ahorcado")
  print("[2] Otros juegos")
  print("[3] Salir \n")
  opcion = str(input("Ingrese una Opcion : "))
  return opcion

def Menu_El_Ahorcado():
    """ Esta Función mostrara el título del juego "El ahorcado" y un menú para que el usuario seleccione la categoría o regrese al menú anterior 
    """
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
  La funcion recibe una funcion que ejecutara nuevamente pero antes
  te avisara que habias escogido una funcion invalida
  """
  limpiar_consola()
  print("Por favor ingrese una opción valida")
  print("")
  funcion()

def imprimir_ahorcado(errores):
  """
  Esta funcion imprime el ahorcado deacuerdo a los errores cometidos con el limite de 6 errores
  """
  if errores == 0:
    print(''' 
      ___________
    |   ______  |
    |   |    |  |
    |        |  |
    |        |  |
    |        |  |
    |        |  |
    |___________|''')
  elif errores == 1:
    print('''
      ___________
    |   _____   |
    |   |   |   |
    |   O   |   |
    |       |   |
    |       |   |
    |       |   |
    |___________|''')
  elif errores == 2:
    print('''
      ___________
    |   _____   |
    |   |   |   |
    |   O   |   |
    |   |   |   |
    |       |   |
    |       |   |
    |___________|''')
  elif errores == 3:
    print('''
      ___________
    |   _____   |
    |   |   |   |
    |   O   |   |
    |  /|   |   |
    |       |   |
    |       |   |
    |___________|''')
  elif errores == 4:
    print('''
      ___________
    |   _____   |
    |   |   |   |
    |   O   |   |
    |  /|\  |   |
    |       |   |
    |       |   |
    |___________|''')
  elif errores == 5:
    print('''
      ___________
    |   _____   |
    |   |   |   |
    |   O   |   |
    |  /|\  |   |
    |  /    |   |
    |       |   |
    |___________|''')
  elif errores == 6:
    print('''
      ___________
    |   _____   |
    |   |   |   |
    |   O   |   |
    |  /|\  |   |
    |  / \  |   |
    |       |   |
    |___________|''')

def jugar(adivinar, categoria:str): 
  """
  Esta funcion recibe como parametro una lista de caracteres
  en mayusculas y comenzara a iterar letra por letra
  de la palabra a advinar buscando similitudes con las letras que vamos ingresando 
  Si no encuentra letras coincidentes imprimira un guion bajo en su lugar.
  
  Parámetros:
    adivinar -- letras_ingresadas o frase que se utilizara para iterar(Solo
    pueden ser letras_ingresadas) 

  La funcion muestra las letras erroneas

  Solo permite ingresar una letra a la vez para comparar
  
  Si ingresas una letra que no esta en la frase se contara como 
  un error

  Si el parametro a adivinar es una frase, el "espacio" no se
  considerara como un guion.

  La funcion termina si al iterar no encuentra guiones bajos, entonces
  ganas el juego, si cometes 6 intentos tambien acaba la funcion y pierdes el juego
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
        imprimir_ahorcado(intentos)
        guiones = 0
        print("")
        print(f"Errores: ", end=" ")
        for error in errores:
           print(f"[ {error} ]",end=" ")
        print("")
        for letra in adivinar:
            if letra in letras_ingresadas: 
                print(letra,end=" ")
            elif letra == " ":
                print("  ",end=" ") 
            else:
                print("_",end=" ")
                guiones +=1

        print("\n")
        print(f"Intentos restantes: {6-intentos}")

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

        if letra_repetida(tu_letra, letras_ingresadas) == True:
          
          if len(tu_letra) >1:
            limpiar_consola()
            print("")
            print("Solo una letra a la vez por favor\n")
            sleep(1.5)
          
          elif validar_especiales(tu_letra) == False:
            limpiar_consola()
            print("")
            print("Por favor solo ingresa letras\n")
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
          limpiar_consola()
          print("")
          print("Ya ingresaste esa letra, ingresar una diferente\n")
          sleep(2)

      else:
        print("Intentos agotados, perdiste el juego")
        imprimir_ahorcado(intentos)
        sleep(2)
        limpiar_consola()
        break

def volver_jugar(adivinar):
  """
  Esta funcion pregunta al usuario si quisiera volver a la
  sala principal o desea salir completamente del juego
  """
  dibujo.volver()
  valor = input("(SI/NO) : ").upper()
  if valor == "SI":
    limpiar_consola()
    adivinar()
  if valor == "NO":
    limpiar_consola()
    print("Adiós!!")
    print('''
    
  ▄█▀█▄           ██
▄████████▄     ▄▀█▄▄▄▄
██▀▼▼▼▼▼     ▄▀ █▄▄   
█████▄▲▲▲     ▄▄▀   ▀▄
██████▀▀▀▀   ▀        ▀▀
        VUELVE PRONTOOOO!
''')
  else:
    limpiar_consola()
    print("")
    print("Por favor solo responda 'Si' o 'NO'\n")
    
    sleep(2)
    limpiar_consola()
    volver_jugar(adivinar)

def opcion1():

  """
  Esta funcion ejecuta el menu del juego del ahorcado y permite
  escoger cualquiera de las categorias disponibles.
  """
  opcion = Menu_El_Ahorcado()
  if opcion == "1":
    limpiar_consola()

    jugar(choice(categoria.peliculas_mas_vistas),"Peliculas Famosas")

  elif opcion == "2":
    limpiar_consola()

    jugar(choice(categoria.videos_juegos),"Videojuegos")

  elif opcion == "3":
    limpiar_consola()

    jugar(choice(categoria.frases_de_disney),"Frases de Disney")

  elif opcion == "4":
    limpiar_consola()

    jugar(choice(categoria.deportes),"Deportes")

  elif opcion == "5":

    jugar(choice(categoria.mujeres_historicas),"Mujeres Historicas")

  elif opcion == "6":
    limpiar_consola()

    jugar(choice(categoria.refranes),"Refranes")

  else:
    limpiar_consola()
    error(opcion1)

def opcion2():
  limpiar_consola()
  print("Proximamente...\n")
  dibujo.proximamente()
  sleep(2)

def opcion3():
  limpiar_consola()
  print("Adiós!!")
  print('''

  ▄█▀█▄           ██
▄████████▄     ▄▀█▄▄▄▄
██▀▼▼▼▼▼     ▄▀ █▄▄   
█████▄▲▲▲     ▄▄▀   ▀▄
██████▀▀▀▀   ▀        ▀▀
        VUELVE PRONTOOOO!
''')


