import os
import sys


def clear_console():
	# Detectar el sistema operativo
	os_name = os.name

	# Limpiar la consola según el sistema operativo
	if os_name == 'posix':  # macOS y Linux
		os.system('clear')
	elif os_name == 'nt':  # Windows
		os.system('cls')
	else:
		print("No se pudo detectar el sistema operativo para limpiar la consola.")


# Tu código principal
hola = "Como estas"
print(id(hola))

# Pausa y luego limpia la consola
input("Presiona Enter para continuar...")
clear_console()
