import pyfiglet
from colorama import Fore, Style

from colorama import init
init (autoreset=True)


text = "bosta"

ascii_art = pyfiglet.figlet_format(text, font="slant")

print (Fore.CYAN + Style.BRIGHT + ascii_art)