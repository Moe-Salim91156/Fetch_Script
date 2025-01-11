import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def log_message(message, log_level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_colors = {
        "INFO": Fore.LIGHTGREEN_EX,
        "WARNING": Fore.YELLOW,
        "HINTS": Fore.MAGENTA,
        "ERROR": Fore.RED,
        "DEBUG": Fore.BLUE,
    }

    color = log_colors.get(log_level, Fore.WHITE)

    colored_message = f"{color}[{timestamp}] [{log_level}] {message}{Style.RESET_ALL}"
    print(colored_message)
    
    with open("output_files/log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] [{log_level}] {message}\n")

