from time import sleep
import funcion
def logo():
  """
  Dibuja el logo de "UTEC GAMES" en pantalla.
  """
  print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  
█  ▄  ▄ ▄▄▄ ▄▄▄ ▄▄▄   ▄▄▄  ▄▄▄ ▄▄ ▄▄ ▄▄▄ ▄▄▄  █ 
█  █  █  █  █▄▄ █     █ ▄▄ █▄█ █ █ █ █▄▄ █▄▄  █
█  █▄▄█  █  █▄▄ █▄▄   █▄▄█ █ █ █   █ █▄▄ ▄▄█  █
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
                          """)

def logo_ahorcado():
  """
  Dibuja el logo de "UTEC GAMES" en pantalla.
  """
  print("""
  ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄  ▄▄▄     
  █▄█ █▄█ █ █ █▄▄▀ █   █▄█ █  █ █ █    
  █ █ █ █ █▄█ █ ▀▄ █▄▄ █ █ █▄▄▀ █▄█    
══════════════════════════════════════
                          """)

def ahorcado():
  """
  Trabaja con la función "sleep" del módulo "time".
  Borra la consola e imprime la palabra "Ahorcado" por unos breves segundos.
  """
  funcion.limpiar_consola()
  print('''
▀ ▀ ▀   █▀▀█ █  █ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █▀▀▄ █▀▀█   █ █ █
█ █ █   █▄▄█ █▄▄█ █  █ █▄▄▀ █   █▄▄█ █  █ █  █   █ █ █
█ █ █   █  █ █  █ █▄▄█ █ ▀▄ █▄▄ █  █ █▄▄▀ █▄▄█   ▄ ▄ ▄
               ''')
  sleep(0.75)
  funcion.limpiar_consola()

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
    funcion.limpiar_consola()
    print(figura)
    sleep(0.1)
  sleep(0.7)
  funcion.limpiar_consola()
  ahorcado()

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
        funcion.limpiar_consola()
        print(figura)
        sleep(0.1)
    sleep(0.5)
    funcion.limpiar_consola()

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
    funcion.limpiar_consola()
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
    sleep(1)
    funcion.limpiar_consola()

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

def pistola():
    print(''' ⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣤⣤
⠀⠀⢶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿  
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠠⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠛⠋⠉⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⢠⣿⡀⠀⠀⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣙⣂⣠⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠛⠛⠛⠛⠻⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    sleep(2)

def flecha():
    print('''
                           ▄█▄
                         ▄█████▄
                       ▄█████████▄
                           ███
                           ███
██████████████████████████████                 
  ''')

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
  las opciones disponibles son:
  1. "Ingresar opcion valida"
  2. "Solo responder 'si' o 'no'
  3. "No repetir letras"
  4. "Solo ingresa una letra a la vez"
  5. "Solo ingresa letras del abecedario"
  """
  if opcion == 1:
    print('''
       __^__                                      __^__
      ( ___ )------------------------------------( ___ )
       | / |                                      | \ |
       | / |  Por favor ingrese una opción valida | \ |
       |___|                                      |___|
      (_____)------------------------------------(_____) ''')

  elif opcion == 2:
    print('''                     
  ╔═══════════════════════════════════════════╗ 
  ║  Por favor solo responder "si" o "no" :D  ║ 
  ╚═══════════════════════════════════════════╝ ''')
  elif opcion == 3:
    print('''
  ╔═══════════════════════════════════════════════════════════╗ 
  ║ Ya ingresaste esa LETRA, ingresa una DIFERENTE ¯\_(ツ)_/¯ ║ 
  ╚═══════════════════════════════════════════════════════════╝
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


def animacion_ahorcado(adivinar):
  funcion.limpiar_consola()
  print("Intentos agotados, perdiste el juego\n")
  print(f"La palabra era '{adivinar}'")
  print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █    ____   █
    █   O═══╝ | █
    █  /|\    | █
    █  / \    | █
    █         | █
    █           █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
  sleep(1)
  funcion.limpiar_consola()
  print("Intentos agotados, perdiste el juego\n")
  print(f"La palabra era '{adivinar}'")
  print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █    _____  █
    █   O__|  | █
    █  /|\    | █
    █  / \    | █
    █         | █
    █           █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
  sleep(1)
  funcion.limpiar_consola()
  print("Intentos agotados, perdiste el juego\n")
  print(f"La palabra era '{adivinar}'") 
  print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █     _____ █
    █     _|  | █
    █   O/    | █
    █  /|\    | █
    █  / \    | █
    █           █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
  sleep(1)
  funcion.limpiar_consola()
  print("Intentos agotados, perdiste el juego\n")
  print(f"La palabra era '{adivinar}'")
  print('''
     ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █     _____ █
    █     /   | █
    █   O/    | █
    █  /|\    | █
    █  / \    | █
    █           █
    █▄▄▄▄▄▄▄▄▄▄▄█''')
  sleep(1)
  funcion.limpiar_consola()
  print("Intentos agotados, perdiste el juego\n")
  print(f"La palabra era '{adivinar}'")
  print('''
    ▄▄▄▄▄▄▄▄▄▄▄▄
    █ UTEC      █
    █    _____  █
    █    |DEAD| █
    █    O    | █
    █   /|\   | █
    █   / \   | █
    █         | █
    █▄▄▄▄▄▄▄▄▄▄▄█''') 


