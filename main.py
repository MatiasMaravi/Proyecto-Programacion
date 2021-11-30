import funcion as F
import dibujo as D
import opciones as OP


def main():
    Opcion_de_Menu = D.menu_utec()
    if Opcion_de_Menu == "1":
        D.introduccion()
        OP.opcion1()
        F.volver_sala(main)
    elif Opcion_de_Menu == "2":
        OP.opcion2()
        main()
    elif Opcion_de_Menu == "3":
        OP.opcion3()
    else:
        D.error(1)
        main()

main()




  