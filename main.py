GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Definição das linhas
top = [
    (21, GREEN + "'c." + RESET),
    (19, GREEN + ",xMM." + RESET),
    (17, GREEN + ".OMMMo" + RESET),
    (17, GREEN + "OMMM0," + RESET),
    (7, GREEN + ".;loddo:' loolodol;." + RESET)
]

middle = [
    (5, GREEN + " cKMMMMMMMMMMNWMMMMMW0:" + RESET),
    (4, YELLOW + ".KMMMMMMMMMMNWMMMMMMMWd." + RESET),
    (3, YELLOW + " cKMMMMMMMMMMNWMMMMMWX." + RESET),
    (3, RED + ";KMMMMMMMMMMNWMMMMMMM:" + RESET),
    (3, RED + ":KMMMMMMMMMNWMMMMMMMM:" + RESET),
    (4, RED + "kMMMMMMMMMNWMMMMMMMMWd." + RESET),
    (4, PURPLE + ".XMMMMMMMMMMNWMMMMMMMWMK:" + RESET),
    (5, PURPLE + ".XMMMMMMMMMNWMMMMMMMWMK." + RESET)
]

bottom = [
    (7, BLUE + "cKMMMMMMMMMMNWMMMMMd" + RESET),
    (8, BLUE + "cKMMMMMMMMMNMMMMk." + RESET),
    (9, BLUE + ".cooc,.  .,coo:." + RESET)
]

def print_lines(lines):
    """Imprime as linhas"""
    for spaces, line in lines:
        print(" " * (37 + spaces) + line)

# Imprimindo as linhas
print("\n"*7)
print_lines(top)
print_lines(middle)
print_lines(bottom)
print("\n"*7)
