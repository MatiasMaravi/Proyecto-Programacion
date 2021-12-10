from time import sleep #Importa una función para dormir al programa por un número de segundos. 
import funcion as F # Importa las funciones del archivo función. Se apoda F.
import dibujo as D
def reemplazar(ruta, valores):
  """
  Parametros:

  -ruta --> ruta de una de las historias .txt aleatorias.

  -valores --> diccionario con las palabras que reemplazarán en la historia asignada.

  Esta funcion abre la ruta y reemplaza las palabras que se encuentren en los keys de "valores"
  """
  with open(ruta,'r') as f:
    filedata = f.read()
  for i in valores:
    filedata = filedata.replace(i,valores[i])
  
  texto = ""
  for termino in filedata.split(" "):
    F.limpiar_consola()
    texto += f"{termino} "
    print(texto)
    sleep(0.08)
    
def historia1():
  """
  Esta funcion muestra los inputs de la historia 1 y retorna el diccionario registrado.
  """
  D.menu_mad_story()
  tu_nombre = input("Tu nombre: ")
  cantante_masculino = input("Cantante masculino: ")
  nombre_padre = input("Nombre de tu padre: ")
  animal_mascota = input("Animal de mascota: ") 
  villano_pelicula = input("Villano de una pelicula: ")
  numero = input("Un número de 1 al 20: ")
  establecimiento = input("Establecimiento público: ")
  alimento = input("Un alimento: ")
  parte_del_cuerpo = input("Una parte del cuerpo: ")
  animal_salvaje = input("Animal salvaje: ")
  objeto_deportivo = input("Objeto deportivo: ")
  print("¡Listooo!")
  sleep(1.0)

  valores = { 
              "/tu_nombre/": tu_nombre,
              "/cantante_masculino/": cantante_masculino, 
              "/nombre_padre/": nombre_padre, 
              "/animal_mascota/": animal_mascota,
              "/villano_pelicula/": villano_pelicula,
              "/numero_de_1-20/": numero,
              "/establecimiento/": establecimiento,
              "/alimento/": alimento,
              "/parte_del_cuerpo/": parte_del_cuerpo,
              "/animal_salvaje/": animal_salvaje,
              "/objeto_deportivo/": objeto_deportivo
            }
  return valores

def historia2():
  """
  Esta funcion muestra los inputs de la historia 2 y retorna el diccionario registrado.
  """
  D.menu_mad_story()
  nombre_madre = input("Nombre de tu madre: ")
  nombre_mascota = input("Nombre de tu mascota: ")
  estacion_del_año = input("Estación del año: ")
  establecimiento = input("Establecimiento público: ")
  festividad_del_peru = input("Festividad del Perú: ")
  ciudad_del_peru = input("Ciudad del Perú: ")
  animal_salvaje = input("Animal salvaje: ")
  print("¡Listooo!")
  sleep(1.0)
  valores = {
            "/nombre_madre/": nombre_madre,
            "/nombre_mascota/": nombre_mascota,
            "/estacion_del_año/": estacion_del_año,
            "/establecimiento/": establecimiento,
            "/festividad_del_peru/": festividad_del_peru,
            "/animal_salvaje/": animal_salvaje,
            "/ciudad_del_peru/": ciudad_del_peru
            }
  return valores

def historia3():
  """
  Esta funcion muestra los inputs de la historia 3 y retorna el diccionario registrado.
  """
  D.menu_mad_story()
  
  tu_nombre = input("Ingrese tu Nombre") 

  nombre_masculino= input("Ingrese un nombre Masculino")

  distrito_p = input("ingrese un Distrito") 

  a_nimal = input("Ingrese un animal domestico") 

  nombre_mascota = input("Ingrese un nombre de una mascota ") 

  nombre_animal = input("Ingrese un animal salvaje") 
  print("¡Listooo!")
  sleep(1.0)
  valores = {
            "/tu_nombre/": tu_nombre,
            "/nombre_masculino/": nombre_masculino ,
            "/distrito_p/": distrito_p,
            "/a_nimal/": a_nimal,
            "/nombre_mascota/": nombre_mascota,
            "/nombre_animal/": nombre_animal,
            }

  return valores


def historia4():
  """
  Esta funcion muestra los inputs de la historia 4 y retorna el diccionario registrado.
  """
  D.menu_mad_story()
  nombre_pueblo = input("Ingrese nombre de un pueblo") 

  un_familiar = input("Ingrese un miembro de tu familia")

  un_lugar = input("ingrese un lugar peligroso") 

  cualquir_persona = input("Ingrese un cargo politico") 

  un_arma = input("Ingrese nombre de una arma") 

  tipo_de_voz = input("Ingrese tipo de voz") 
 
  print("¡Listooo!")
  sleep(1.0)
  valores = {
            "/nombre_pueblo/": nombre_pueblo,
            "/un_familiar/": un_familiar ,
            "/un_lugar/": un_lugar,
            "/cualquir_persona/": cualquir_persona,
            "/un_arma/": un_arma,
            "/tipo_de_voz/": tipo_de_voz,
            }

  return valores


def historia5():
  """
  Esta funcion muestra los inputs de la historia 5 y retorna el diccionario registrado.
  """
  D.menu_mad_story()

  Nombre_Niño = input("Ingresa un nombre de persona")

  nombre_colegio = input("Ingresa un nombre de colegio")

  fenomeno_natural = input("Ingrese un fenomeno fenomeno_natural")

  fecha = input("Ingresa una fecha DD/MM/NN")

  nombre_truco = input("¿Que nombre le pondrías a un truco de magía?")
  print("¡Listooo!")
  sleep(1.0)
  valores = {
            "/Nombre_Niño/": Nombre_Niño,
            "/nombre_colegio/": nombre_colegio ,
            "/fenomeno_natural/": fenomeno_natural,
            "/fecha/": fecha,
            "/nombre_truco/": nombre_truco,
            }
            
  return valores
