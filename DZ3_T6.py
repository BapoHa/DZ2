import sys
from pathlib import Path

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("Помилка: встановіть colorama командою: pip install colorama")
    sys.exit(1)


def visualize_directory(directory, prefix=""):
    entries = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "

        if entry.is_dir():
            print(prefix + connector + Fore.YELLOW + Style.BRIGHT + entry.name)
            visualize_directory(entry, prefix + extension)
        else:
            print(prefix + connector + Fore.CYAN + entry.name)


if len(sys.argv) != 2:
    print(Fore.RED + "Використання: python <шлях до файлу DZ3_T6.py> <шлях до директорії>")
    sys.exit(1)

target = Path(sys.argv[1])

if not target.exists():
    print(Fore.RED + f"Шлях не існує: {target}")
    sys.exit(1)

if not target.is_dir():
    print(Fore.RED + f"Це не директорія: {target}")
    sys.exit(1)

print(Fore.YELLOW + Style.BRIGHT + str(target.resolve()))
visualize_directory(target)
