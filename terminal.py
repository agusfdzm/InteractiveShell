import cmd
from colorama import init, Fore, Style
import commands

init(autoreset=True)

class MiTerminal(cmd.Cmd):
    intro = Fore.CYAN + "Bienvenido a Interactive Term. Escribe 'help' para ver los comandos." + Style.RESET_ALL
    prompt = Fore.GREEN + ">>> " + Style.RESET_ALL

    def do_hola(self, arg):
        return commands.hola(arg)

    def do_sumar(self, arg):
        return commands.sumar(arg)

    def do_cls(self, arg):
        return commands.cls(arg)

    def do_salir(self, arg):
        return commands.salir(arg)

    def emptyline(self):
        pass

    def default(self, line):
        print(Fore.RED + f"Comando desconocido: {line}")
