import funcion as F
import dibujo as D

def main():
  F.limpiar_consola()
  Opcion_de_Menu = D.menu_utec()
  if Opcion_de_Menu == "1":
    D.introduccion()
    F.opcion1()
    F.volver_sala(main)  
  elif Opcion_de_Menu == "2":
    F.opcion2()
    main()
  elif Opcion_de_Menu == "3":
    F.opcion3()
  else:
    D.error(1)
    main()

main()
