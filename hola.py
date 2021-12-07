from time import sleep #Importa una función para dormir al programa por un número de segundos. 
import dibujo as D #Importa funciones de los dibujos. Se apoda D.


def introducir_datos():
  """
  -Esta funcion pide al usuario que introduzca los datos correspondientes que reemplazarán a los términos de la historia en diccionario "valores".
  """
  #Inputs del cuento1: 
  #Inputs de la historia 1
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
            
  # Inputs de la historia 2
  nombre_madre = input("Nombre de tu madre: ")
  nombre_mascota = input("Nombre de tu mascota: ")
  estacion_del_año = input("Estación del año: ")
  establecimiento = input("Establecimiento público: ")
  festividad_del_peru = input("Festividad del Perú: ")
  ciudad_del_peru = input("Ciudad del Perú: ")

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

def reemplazar(ruta, valores):
  """
  Parametros:

  -ruta --> ruta de una de las historias .txt aleatorias.

  -valores --> diccionario con los datos que reemplazarán en la historia asignada.

  Esta funcion abre la ruta y reemplaza las palabras que se encuentren en los keys de "valores"
  """
  with open("historias/historia2.txt",'r') as f:
    filedata = f.read()
  for i in valores:
    filedata = filedata.replace(i,valores[i])
  
  texto = ""
  for termino in filedata.split(" "):
    texto += termino
    print(termino)
    sleep(0.1)
  
