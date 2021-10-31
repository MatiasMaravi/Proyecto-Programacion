import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma


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


def jugar(adivinar): 
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
  palabra = "" 
  while True:
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
          print("Felicidades ganaste")
          break
      print("")
      tu_letra= input("Introduce tu letra: ").upper()

      if len(tu_letra) > 1:
          print("Por favor solo una letra a la vez")
      else:    
          palabra+=tu_letra


#Esta funcion permite que el juego termine despues de los 6 intentos.
def intentos(errores):
