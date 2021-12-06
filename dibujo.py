from time import sleep #Importa una función para dormir al programa por un número de segundos.
import funcion as F #Importa el archivo llamado función donde se encuentran todas nuestras funciones del juego.

#LOGOS

def menu_utec():
  """
  Dibuja el logo de "UTEC GAMES" en pantalla.
 
  Esta Función mostrará el título del juego "UTEC GAMES" y un menú para que el usuario 
  seleccione la categoría o regrese al menú anterior. 
  Retorna la opcion ingresada.
 """
  F.limpiar_consola()
  print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  
█  ▄  ▄ ▄▄▄ ▄▄▄ ▄▄▄   ▄▄▄  ▄▄▄ ▄▄ ▄▄ ▄▄▄ ▄▄▄  █ 
█  █  █  █  █▄▄ █     █ ▄▄ █▄█ █ █ █ █▄▄ █▄▄  █
█  █▄▄█  █  █▄▄ █▄▄   █▄▄█ █ █ █   █ █▄▄ ▄▄█  █
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
                          """)
  print("""
Seleccione una categoría:
══════════════════════════

1. Juego del ahorcado
2. Mad Story
3. Otros juegos
4. Leaderboard
5. Salir 
  """)
  opcion = str(input("Ingrese una Opcion --→ "))
  return opcion

def menu_ahorcado():
  """
  Dibuja el logo de "UTEC GAMES" en pantalla.
     
  Esta función limpia la consola y muestra el título del juego "El ahorcado", 
  además muestra un menú para que el usuario seleccione la categoría o regrese al menú anterior.
  Retorna la categoria escogida.
  
  """
  F.limpiar_consola()
  print("""
  ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄  ▄▄▄     
  █▄█ █▄█ █ █ █▄▄▀ █   █▄█ █  █ █ █    
  █ █ █ █ █▄█ █ ▀▄ █▄▄ █ █ █▄▄▀ █▄█    
══════════════════════════════════════

 Elige una categoría:  
 ═══════════════════════

 1. Peliculas Famosas  
 2. Videojuegos 
 3. Frases de Disney  
 4. Deportes 
 5. Mujeres Historicas  
 6. Refranes 
 7. Regresar a la sala principal

 (Si quieres ver las reglas del juego ingresa "reglas")
  """)
  
  opc = str(input( "Elija una Opcion :D --→ ")).upper() 
  return opc

def ahorcadooo():
  """
  Trabaja con la función "sleep" del módulo "time".
  Borra la consola e imprime la palabra "Ahorcado" por unos breves segundos.
  """
  F.limpiar_consola()
  print('''
▀ ▀ ▀   █▀▀█ █  █ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █▀▀▄ █▀▀█   █ █ █
█ █ █   █▄▄█ █▄▄█ █  █ █▄▄▀ █   █▄▄█ █  █ █  █   █ █ █
█ █ █   █  █ █  █ █▄▄█ █ ▀▄ █▄▄ █  █ █▄▄▀ █▄▄█   ▄ ▄ ▄
               ''')
  sleep(0.75)
  F.limpiar_consola()

def introduccion():
  """
  Trabaja con la función "sleep" del módulo "time".
  Dibuja en pantalla una animación de la palabra "El juego de".
  """
  figuras = [
        '''        
   █▀▀ █
   █▀▀ █
   ▀▀▀ ▀▀▀
   ''', '''   
   █▀▀ █    ▀▀█▀ █  █ █▀▀ █▀▀  █▀▀█
   █▀▀ █      █  █  █ █▀▀ █ ▀█ █  █
   ▀▀▀ ▀▀▀  ▀▀▀  ▀▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀▀
                  ''', ''' 
   █▀▀ █    ▀▀█▀ █  █ █▀▀ █▀▀  █▀▀█   █▀▀▄ █▀▀ █
   █▀▀ █      █  █  █ █▀▀ █ ▀█ █  █   █  █ █▀▀ █
   ▀▀▀ ▀▀▀  ▀▀▀  ▀▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀▀   ▀▀▀  ▀▀▀ ▀▀▀  '''
    ]

  for figura in figuras:
    F.limpiar_consola()
    print(figura)
    sleep(0.1)
  sleep(0.7)
  F.limpiar_consola()
  ahorcadooo()

def a_jugar():
    """
    Trabaja con la función "sleep" del módulo "time".
    Dibuja en pantalla una animación de la palabra "A jugar".
    """
    figuras = [
    '''
   █▀▀▀█        
   █▄▄▄█                                 
   █   █                                           ''', '''
   █▀▀▀█    ▀▀█▀  █  █  
   █▄▄▄█      █   █  █  
   █   █    ▄▄█   █▄▄█                             ''', '''
   █▀▀▀█    ▀▀█▀  █  █  █▀▀▀▀  █▀▀▀█  █▀▀▀█    
   █▄▄▄█      █   █  █  █  ▄▄  █▄▄▄█  █▄▄▄█    
   █   █    ▄▄█   █▄▄█  █▄▄▄█  █   █  █  ▀▄        ''', '''
   █▀▀▀█    ▀▀█▀  █  █  █▀▀▀▀  █▀▀▀█  █▀▀▀█    █  █
   █▄▄▄█      █   █  █  █  ▄▄  █▄▄▄█  █▄▄▄█    █  █
   █   █    ▄▄█   █▄▄█  █▄▄▄█  █   █  █  ▀▄    ▄  ▄'''
    ]

    for figura in figuras:
        F.limpiar_consola()
        print(figura)
        sleep(0.1)
    sleep(0.5)
    F.limpiar_consola()



def reglas():
  """
  Imprimira las reglas en pantalla y pedira al usuario que ingrese alguna 
  tecla para continuar
  """
  print("""
 ▄▄▄▄ ▄▄▄ ▄▄▄  ▄   ▄▄▄ ▄▄▄   
 █▄▄▀ █▄▄ █ ▄▄ █   █▄█ █▄▄
 █ ▀▄ █▄▄ █▄▄█ █▄▄ █ █ ▄▄█
═══════════════════════════
                          """)
  print("""
1. Tienes que adivinar la palabra o frase relacionada a
la categoria que escojas.

2. Solo puedes ingresar una letra a la vez.

3. Solo puedes ingresar letras o números (No tildes).

4. Si ya ingresaste una letra no puedes repetirla.

5. Solo tienes 6 intentos, si ingresas una letra 
que no esté en la frase perderás un intento.

6. Una vez empezado el juego tienes la opcion de escapar 
escribiendo la palabra "salir". 
  """)
  
  input("Presiona enter para continuar: ")

def salvado():
    """
    Dibuja en pantalla el muñeco escapando del juego y celebrando.
    """
    print('''  
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █     
    █   |    |  █        
    █        |  █     SIIIIII
    █        |  █   O/   
    █        |  █  /|         
    █        |  █  / \  
    █▄▄▄▄▄▄▄▄▄▄▄█
            ''')

def volver():
    """
    Dibuja en pantalla un camión que te pregunta si quisieras
    volver a la sala principal
    """
    print('''
──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
───▄▄██▌█ ¿Desea volver a la   ▌
▄▄▄▌▐██▌█ sala principal?      ▌ 
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀(@)▀

''')

def muerte():
    """
    Trabaja con la función "sleep" del módulo "time".
    Limpia la consola y muestra a la muerte llamandote cobarde por rendirte y escapar del juego.
    """
    F.limpiar_consola()
    print('''  
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠄⠄⠈⠙⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿
⣿⣿⣿⣿⡿⠃⠄⠄⠄⢀⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠈⢿
⣿⣿⣿⡟⠄⠄⠄⠄⠐⢻⣿⣿⣿⣷⡄⠄⠄⠄⠄⠄⠄⠈
⣿⣿⣿⠃⠄⠄⠄⢀⠴⠛⠙⣿⣿⡿⣿⣦⠄⠄⠄⠄⠄⠄
⣿⣿⠃⠄⢠⡖⠉⠄⠄⠄⣠⣿⡏⠄⢹⣿⠄⠄⠄⠄⠄⢠
⣿⠃⠄⠄⢸⣧⣤⣤⣤⢾⣿⣿⡇⠄⠈⢻⡆⠄⠄⠄⠄⣾
⠁⠄⠄⠄⠈⠉⠛⢿⡟⠉⠉⣿⣷⣀⠄⠄⣿⡆⠄⠄⢠⣿
⠄⠄⠄⠄⠄⠄⢠⡿⠿⢿⣷⣿⣿⣿⣿⣿⠿⠃⠄⠄⣸⣿
⠄⠄⠄⠄⠄⢀⡞⠄⠄⠄⠈⣿⣿⣿⡟⠁⠄⠄⠄⠄⣿⣿
⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⢀⣿⣿⡟⠄⠄⠄⠄⠄⢠⣿⣿
⠄⠄⠄⠄⠄⠘⠄⠄⠄⢀⡼⠛⠉⠄⠄⠄⠄⠄⠄⣼⣿⣿
⠄⠄⠄⠄⠄⡇⠄⠄⢀⠎⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿
⠄⠄⠄⠄⢰⠃⠄⢀⠎⠄⠄⠄COBARDE!!! ⠙ ''')
    sleep(2)
    F.limpiar_consola()

def proximamente():
    """
    Trabaja con la función "sleep" del módulo "time".
    Dibuja en pantalla una animación de "signos de interrogacion".
    """
    sleep(0.1)
    print('''     ╔═══╗''', end="")
    print('''    ╔═══╗''', end="")
    print('''    ╔═══╗''')
    sleep(0.1)
    print('''     ║╔═╗║''', end="")
    print('''    ║╔═╗║''', end="")
    print('''    ║╔═╗║''')
    sleep(0.1)
    print('''     ╚╝╔╝║''', end="")
    print('''    ╚╝╔╝║''', end="")
    print('''    ╚╝╔╝║''')
    sleep(0.1)
    print('''       ║╔╝''', end="")
    print('''      ║╔╝''', end="")
    print('''      ║╔╝''')
    sleep(0.1)
    print('''       ╔╗ ''', end="")
    print('''      ╔╗ ''', end="")
    print('''      ╔╗ ''')
    sleep(0.1)
    print('''       ╚╝ ''', end="")
    print('''      ╚╝ ''', end="")
    print('''      ╚╝ ''')

def despedida():
    """
    Dibuja en pantalla un muñeco escapando de un cocodrilo despidiendose.
    """
    print('''

  ▄█▀█▄           ██
▄████████▄     ▄▀█▄▄▄▄
██▀▼▼▼▼▼     ▄▀ █▄▄   
█████▄▲▲▲     ▄▄▀   ▀▄
██████▀▀▀▀   ▀        ▀▀
        VUELVE PRONTOOOO!
''')

def error(opcion):
  """
  La funcion recibe como parametro la opcion a pintar en pantalla.
  Las opciones disponibles son:
  1. "Ingresar opcion valida"
  2. "Solo responder 'si' o 'no'
  3. "No repetir letras"
  4. "Solo ingresa una letra a la vez"
  5. "Solo ingresa letras del abecedario"
  """
  F.limpiar_consola()
  if opcion == 1:
    print('''
   __^__                                      __^__
  ( ___ )------------------------------------( ___ )
   | / |                                      | \ |
   | / |  Por favor ingrese una opción valida | \ |
   |___|                                      |___|
  (_____)------------------------------------(_____) ''')
    sleep(2)

  elif opcion == 2:
    print('''                     
╔═══════════════════════════════════════════╗ 
║  Por favor solo responder "si" o "no" :D  ║ 
╚═══════════════════════════════════════════╝ ''')

  elif opcion == 3:
    print('''
╔══════════════════════════════════════════╗ 
║ Ingresa un carácter DIFERENTE ¯\_(ツ)_/¯ ║ 
╚══════════════════════════════════════════╝
  ''')

  elif opcion == 4:
    print('''
╔══════════════════════════════════════════════╗ 
║ Solo UNA letra a la vez por favor ¯\_(ツ)_/¯ ║ 
╚══════════════════════════════════════════════╝
  ''')

  elif opcion == 5:
    print('''
╔══════════════════════════════════════════╗ 
║ Por favor solo ingresa LETRAS ¯\_(ツ)_/¯ ║ 
╚══════════════════════════════════════════╝
  ''')

def imprimir_ahorcado(errores):
    """
    Esta funcion imprime el ahorcado deacuerdo a los errores cometidos con el limite de 6 errores
    """
    if errores == 0:
        print(''' 
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █
    █   |    |  █
    █        |  █
    █        |  █
    █        |  █
    █        |  █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
    elif errores == 1:
        print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █
    █   |    |  █
    █   O    |  █
    █        |  █
    █        |  █
    █        |  █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
    elif errores == 2:
        print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █
    █   |    |  █
    █   O    |  █
    █   |    |  █
    █        |  █
    █        |  █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
    elif errores == 3:
        print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █
    █   |    |  █
    █   O    |  █
    █  /|    |  █
    █        |  █
    █        |  █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
    elif errores == 4:
        print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █
    █   |    |  █
    █   O    |  █
    █  /|\   |  █
    █        |  █
    █        |  █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
    elif errores == 5:
        print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █
    █   |    |  █
    █   O    |  █
    █  /|\   |  █
    █  /     |  █
    █        |  █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
    elif errores == 6:
        print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █   ______  █
    █   |    |  █
    █   O    |  █
    █  /|\   |  █
    █  / \   |  █
    █        |  █
    █▄▄▄▄▄▄▄▄▄▄▄█''')


def introduccion_madstory():
  """
  Trabaja con la función "sleep" del módulo "time".
  Dibuja en pantalla la animación del título del juego "Mad Story".
  """
  F.limpiar_consola()
  sleep(0.25)
  print('''\n    ██▄▄██  █▀▀▀█  █▀▀▀▄''')
  sleep(0.1)
  print('''    █ ▀▀ █  █▄▄▄█  █   █''')
  sleep(0.1)
  print('''    █    █  █   █  █▄▄▄▀
  ════════════════════════\n''')

  sleep(0.3)

  print('''                           █▀▀▀▀  █████  █████  █▀▀▀█  █   █''')
  sleep(0.1)
  print('''                           █▄▄      █    █   █  █▄▄▄█  ▀▄▄▄▀''')
  sleep(0.1)
  print('''                             ▀▀█    █    █   █  █ ▀▄     █''')
  sleep(0.1)
  print('''                           ▄▄▄▄█    █    █████  █   █    █
                      ═════════════════════════════════════\n''')
  sleep(0.75)
  F.limpiar_consola()