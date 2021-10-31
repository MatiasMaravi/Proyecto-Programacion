import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma
import categoria #importamos las listas 
import random

#Aqui van sus funciones no olviden luego yo lo ordeno en el main


def limpiar_consola(): 
  """
  Esta funcion limpia la consola dependiendo 
  que sistema operativo estes usando
  """
  if platform.system() == "Windows": 
      os.system("cls")
  else:
      os.system("clear")


def jugar(adivinar: str): 
  """
  Esta funcion recibe como parametro una palabra
  en mayusculas y comenzara a iterar letra por letra
  de la palabra a advinar buscando similitudes con las letras que 
  vayamos ingresando, si no encuentra letras coincidentes
  imprimira un guion bajo en su lugar.
  
  Parámetros:
    adivinar -- palabra o frase que se utilizara para iterar(Solo
    pueden ser letras) 

  Si al iterar no encuentra guiones bajos la funcion terminara.
  
  Si el parametro a adivinar es una frase, el "espacio" no se
  considerara como un guion.

  Solo permite ingresar una letra a la vez para comparar
  """
  adivinar = adivinar.upper() 
  errores = 0 
  palabra = "" 
  while True:
      if errores < 6 :
          guiones = 0 
          for letra in adivinar:
              if letra in palabra: 
                  print(letra,end=" ")
              elif letra == " ":
                  print("  ",end=" ") 
              else:
                  print("_",end=" ")
                  guiones +=1
          if guiones == 0: 
              print("") 
              print("Felicidades, ganaste")
              break
          print("")
          tu_letra = input("Introduce tu letra: ").upper() 
          if len(tu_letra) >1:
            limpiar_consola()
            print("Solo una letra a la vez por favor")          
          elif tu_letra not in adivinar:
              limpiar_consola()
              errores += 1          
          else:
            limpiar_consola()
            palabra += tu_letra
      else:
          break
  return errores


def intentos(intento): 
  """"
  Esta funcion permite terminar el juego en solo 6 intentos.
  Para ellos se necesita contar los intentos errados en la variable "errores" en la funcion "jugar".
  
  El parámetro sera "intento" que se utiliza para definir el numero de intentos fallidos

  Si el parametro recibe hasta el numero 6, el resultado denotará como "Juego terminado, perdiste"
  """
  if intento == 6:
      print("Juego terminado, perdiste")


def select_random(lista):
  """
  Esta funcion recibe una lista y devuelve una variable
  aleatoria de esa lista
  """
  return random.choice(lista)

