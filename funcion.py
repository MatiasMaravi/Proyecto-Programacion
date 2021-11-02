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

def jugar(adivinar: str): 
  """
  Esta funcion recibe como parametro una lista de caracteres
  en mayusculas y comenzara a iterar letra por letra
  de la palabra a advinar buscando similitudes con las letras que vamos ingresando 
  Si no encuentra letras coincidentes imprimira un guion bajo en su lugar.
  
  Parámetros:
    adivinar -- letras_ingresadas o frase que se utilizara para iterar(Solo
    pueden ser letras_ingresadas) 

  La funcion muestra las letra erroneas

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
        imprimir_ahorcado(intentos)
        guiones = 0
        print(f"errores: ", end=" ")
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

        if guiones == 0: 
          limpiar_consola()
          print("")
          print("GANASTE!!!!")
          print("Completaste la frase, felicidades")
          break
        
        print("")
        tu_letra = input("Introduce tu letra: ").upper()   

        if letra_repetida(tu_letra, letras_ingresadas) == True:

          if len(tu_letra) >1:
            limpiar_consola()
            print("Solo una letra a la vez por favor")
            print("")
          
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
          print("Ya ingresaste esa letra, ingresar una diferente")

    
      else:
          print("Intentos agotados, perdiste el juego")
          imprimir_ahorcado(intentos)
          break





