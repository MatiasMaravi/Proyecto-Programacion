import funcion as F
import dibujo as D
import opciones as OP


def UTEC_GAMES():
    Opcion_de_Menu = D.menu_utec()
    if Opcion_de_Menu == "1":
        D.introduccion()
        OP.opcion1()
        F.volver_sala(UTEC_GAMES)
    elif Opcion_de_Menu == "2":
        OP.opcion2()
    elif Opcion_de_Menu == "3":
        OP.opcion3()
        UTEC_GAMES()
    elif Opcion_de_Menu == "4":
        OP.opcion4()
    elif Opcion_de_Menu == "5":
        OP.opcion5()
    else:
        D.error(1)
        UTEC_GAMES()

if __name__ == "__main__":
  UTEC_GAMES()


