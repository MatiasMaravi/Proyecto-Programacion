from time import sleep  #Importa una función para dormir al programa por un número de segundos.
import funcion as F  # Importa las funciones del archivo función. Se apoda F.
import dibujo as D


def reemplazar(ruta, valores):
    """
    Parametros:

        -ruta --> ruta de una de las historias.txt aleatorias.

        -valores --> diccionario con las palabras que reemplazarán en la historia asignada.

    Esta funcion abre la ruta y reemplaza las palabras que se encuentren en los keys de "valores". 
    Luego muestra la historia generada en pantalla.
    """
    with open(ruta, 'r') as archivo:
        filedata = archivo.read()
    for i in valores:
        filedata = filedata.replace(i, valores[i])

    texto = ""
    for termino in filedata.split(" "):
        F.limpiar_consola()
        texto += f"{termino} "
        print(texto)
        sleep(0.1)
    input("\nIngresa enter para continuar: ")


def historia1():
    """
    Esta funcion muestra los inputs de la historia 1 y retorna el diccionario registrado.
    """
    D.menu_mad_story()
    tu_nombre = input("Tu nombre: ").capitalize()
    cantante_masculino = input("Cantante masculino: ").capitalize()
    nombre_padre = input("Nombre de tu padre: ").capitalize()
    animal_mascota = input("Animal de mascota: ")
    villano_pelicula = input("Villano de una película: ").capitalize()
    numero = input("Un número de 1 al 20: ")
    establecimiento = input("Establecimiento público: ")
    alimento_plural = input("Un alimento en plural: ")
    parte_del_cuerpo = input("Una parte del cuerpo: ")
    animal_salvaje = input("Animal salvaje: ")
    objeto_deportivo = input("Objeto deportivo: ")
    D.listo()
    sleep(1.0)

    valores = {
        "/tu_nombre/": tu_nombre,
        "/cantante_masculino/": cantante_masculino,
        "/nombre_padre/": nombre_padre,
        "/animal_mascota/": animal_mascota,
        "/villano_pelicula/": villano_pelicula,
        "/numero_de_1-20/": numero,
        "/establecimiento/": establecimiento,
        "/alimento_plural/": alimento_plural,
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
    nombre_madre = input("Nombre de tu madre: ").capitalize()
    nombre_mascota = input("Nombre de tu mascota: ").capitalize()
    estacion_del_año = input("Estación del año: ")
    establecimiento = input("Establecimiento público: ")
    festividad = input("Festividad: ").capitalize()
    ciudad_del_peru = input("Ciudad del Perú: ").capitalize()
    animal_salvaje = input("Animal salvaje: ")
    D.listo()
    sleep(1.0)
    valores = {
        "/nombre_madre/": nombre_madre,
        "/nombre_mascota/": nombre_mascota,
        "/estacion_del_anio/": estacion_del_año,
        "/establecimiento/": establecimiento,
        "/festividad/": festividad,
        "/animal_salvaje/": animal_salvaje,
        "/ciudad_del_peru/": ciudad_del_peru
    }
    return valores


def historia3():
    """
    Esta funcion muestra los inputs de la historia 3 y retorna el diccionario registrado.
    """
    D.menu_mad_story()

    tu_nombre = input("Ingrese tu nombre: ").capitalize()

    nombre_masculino = input("Ingrese un nombre masculino: ").capitalize()

    distrito_p = input("Ingrese un distrito: ").capitalize()

    a_nimal = input("Ingrese un animal domestico: ")

    nombre_mascota = input("Ingrese un nombre de una mascota: ").capitalize()

    nombre_animal = input("Ingrese un animal salvaje: ")
    D.listo()
    sleep(1.0)
    valores = {
        "/tu_nombre/": tu_nombre,
        "/nombre_masculino/": nombre_masculino,
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
    adjetivo = input("Ingrese un adjetivo:").capitalize()

    apellido = input("Ingresa el apellido de tu familia: ").capitalize()

    un_lugar = input("Ingrese un distrito o ciudad: ").capitalize()

    nombre_presidente = input(
        "Ingrese el nombre del presidente que más odias:").capitalize()

    un_arma = input("Ingrese nombre de una arma: ")

    tipo_de_voz = input("Ingrese tipo de voz: ")

    D.listo()
    sleep(1.0)
    valores = {
        "/adjetivo/": adjetivo,
        "/apellido/": apellido,
        "/un_lugar/": un_lugar,
        "/nombre_presidente/": nombre_presidente,
        "/un_arma/": un_arma,
        "/tipo_de_voz/": tipo_de_voz,
    }

    return valores


def historia5():
    """
    Esta funcion muestra los inputs de la historia 5 y retorna el diccionario registrado.
    """
    D.menu_mad_story()

    Nombre_Niño = input("Ingresa un nombre de tu tío: ").capitalize()
    nombre_curso = input("Ingresa tu materia menos favorita:")
    nombre_colegio = input("Ingresa un nombre de colegio: ").capitalize()
    fenomeno_natural = input("Ingrese un fenomeno natural: ")
    año = input("¿En que año te piensas casar?: ")
    nombre_truco = input("¿Qué nombre le pondrías a un truco de magía?: ")

    sleep(1.0)
    D.listo()
    valores = {
        "/Nombre_Ninio/": Nombre_Niño,
        "/nombre_colegio/": nombre_colegio,
        "/fenomeno_natural/": fenomeno_natural,
        "/anio/": año,
        "/nombre_truco/": nombre_truco,
        "/nombre_curso/": nombre_curso,
    }

    return valores
