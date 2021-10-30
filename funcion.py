import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma


#Aqui van sus funciones no olviden luego yo lo ordeno en el main

#Esta funcion limpia la consola
def limpiar_consola(): 
    if platform.system() == "Windows": #valida en que plataforma estas 
        os.system("cls")
    else:
        os.system("clear")

#Esta funcion permite ingresar letra por letra para adivinar la palabra
def jugar(adivinar: str): #El parametro es la palabra a adivinar
    adivinar = adivinar.upper() #El parametro sera todo mayusculas
    palabra = "" #En un comienzo la palabra estara vacia
    while True:
        guiones = 0 #Contador de los guiones que hay
        for letra in adivinar: #Para cada letra de la frase o palabra a adivninar
            if letra in palabra: #Si la letra de adivinar coincide con  la letra que escribimos se imprime
                print(letra,end=" ")
            elif letra == " ":
                print("  ",end=" ") #Si es una frase el espacio no sera un guion
            else:
                print("_",end=" ") #Si la letra no esta escribe un guion en su lugar
                guiones +=1 
        if guiones == 0: #Si todo es letra y no hay guiones ganas el juego
            print("") 
            print("Felicidades ganaste")
            break
        print("")
        tu_letra= input("Introduce tu letra: ").upper()

        if len(tu_letra) > 1:
            print("Por favor solo una letra a la vez")
        else:    
            palabra+=tu_letra

'''
#Esta funcion permite que el juego termine despues de los 6 intetos.
def intentos(intentos):
'''