import funcion as f
import dibujo as d

def main():
  f.limpiar_consola()
  Opcion_de_Menu = f.Menu_UTEC_GAMES()
  if Opcion_de_Menu == "1":
    d.introduccion()
    f.opcion1()
    f.volver_sala(main)  
  elif Opcion_de_Menu == "2":
    f.opcion2()
    main()
  elif Opcion_de_Menu == "3":
    f.opcion3()
  else:
    f.error(main)

main()
