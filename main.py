import cmd
from colorama import init, Fore, Style
import os

# Iniciar colorama
init(autoreset=True)

class MiTerminal(cmd.Cmd):
    intro = Fore.CYAN + "Bienvenido a Interactive Term. Escribe 'help' para ver los comandos." + Style.RESET_ALL
    prompt = Fore.GREEN + ">>> " + Style.RESET_ALL

# Comando 1
    def do_hola(self, arg):
        print(Fore.YELLOW + "¡Hola, humano!")

# Comando 2
    def do_sumar(self, arg):
        try:
            a, b = arg.split()
            print(Fore.MAGENTA + f"Resultado: {int(a) + int(b)}")
        except ValueError:
            print(Fore.RED + "Error: debes escribir dos números. Ejemplo: sumar 3 7")
    
    def do_cls(self, arg):
        os.system('cls' if os.name == 'nt' else 'clear')


# Comando SALIR
    def do_salir(self, arg):
        """Cierra la terminal."""
        print(Fore.CYAN + "Adiós!")
        return True

    # --- Extras ---
    def emptyline(self):
        """Evita repetir el último comando si das ENTER vacío."""
        pass

    def default(self, line):
        """Muestra un error si el comando no existe."""
        print(Fore.RED + f"Comando desconocido: {line}")

# Ejecutar el intérprete
if __name__ == "__main__":
    MiTerminal().cmdloop()
