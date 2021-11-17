import funcion
import dibujo

def main():
  funcion.limpiar_consola()
  Opcion_de_Menu = funcion.Menu_UTEC_GAMES()
  if Opcion_de_Menu == "1":
    dibujo.introduccion()
    funcion.opcion1()
    funcion.volver_jugar(main)  
  elif Opcion_de_Menu == "2":
    funcion.opcion2()
    main()
  elif Opcion_de_Menu == "3":
    funcion.opcion3()
  else:
    funcion.error(main)

main()
funcion.consejos()
