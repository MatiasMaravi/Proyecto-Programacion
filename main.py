from random import choice
import funcion
import categoria

def opcion1():
  opcion = funcion.Menu_El_Ahorcado()
  if opcion == "1":
    funcion.limpiar_consola()
    print("Categoria: Peliculas Famosas")
    funcion.jugar(choice(categoria.peliculas_mas_vistas))

  elif opcion == "2":
    funcion.limpiar_consola()
    print("Categoria: videojuegos")
    funcion.jugar(choice(categoria.videos_juegos))

  elif opcion == "3":
    funcion.limpiar_consola()
    print("Categoria: Frases de Disney")
    funcion.jugar(choice(categoria.frases_de_disney))

  elif opcion == "4":
    funcion.limpiar_consola()
    print("Categoria: Deportes")
    funcion.jugar(choice(categoria.deportes))

  elif opcion == "5":
    funcion.limpiar_consola()
    print("Categoria: Mujeres Historicas")
    funcion.jugar(choice(categoria.mujeres_historicas))

  elif opcion == "6":
    funcion.limpiar_consola()
    print("Categoria: Refranes")
    funcion.jugar(choice(categoria.refranes))
    funcion.volver_jugar(funcion.jugar(choice(categoria.refranes)))
  else:
    print("error")

def main():
  Opcion_de_Menu = funcion.Menu_UTEC_GAMES()

  if Opcion_de_Menu == "1":
    funcion.limpiar_consola()
    opcion1()
    funcion.volver_jugar(main)  
  elif Opcion_de_Menu == "2":
    print("Proximamente...")
  elif Opcion_de_Menu == "3":
    funcion.limpiar_consola()
    print("Adios")
  else:
    print("por favor ingrese una opcion valida")
    
main()
    


  

  


'''
#Para jugar borra la parte de "Aqui pon" y coloca la categoria que quieras jugar(por ejemplo "refranes")
funcion.jugar(choice(categoria.peliculas_mas_vistos))
'''








