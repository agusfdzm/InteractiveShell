import os
from colorama import Fore

def hola(arg):
    print(Fore.YELLOW + "¡Hola, humano!")

def sumar(arg):
    try:
        a, b = arg.split()
        print(Fore.MAGENTA + f"Resultado: {int(a) + int(b)}")
    except ValueError:
        print(Fore.RED + "Error: debes escribir dos números. Ejemplo: sumar 3 7")

def cls(arg):
    os.system('cls' if os.name == 'nt' else 'clear')

def salir(arg):
    print(Fore.CYAN + "Adiós!")
    return True

def help(self, arg):
    if arg:
        cmd, *rest = arg.split()
        if hasattr(self, "do_" + cmd):
            print(getattr(self, "do_" + cmd).__doc__)
        else:
            print(f"No hay ayuda disponible para {cmd}")
    else:
        print("Comandos disponibles:")
        print("  hola   - Muestra un saludo")
        print("  sumar  - Suma dos números")
        print("  cls    - Limpia la pantalla")
        print("  salir  - Sale de la terminal")
