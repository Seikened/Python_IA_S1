animal = "   chanCHito feliz   "
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minusculas
print(animal.strip().capitalize())  # Elimina espacios en blanco y convierte a mayúscula la primera letra
print(animal.title())  # Convierte a mayúscula la primera letra de cada palabra
print(animal.swapcase())  # Convierte a mayúscula las minusculas y viceversa
print(animal.strip())  # Elimina espacios en blanco
print(animal.lstrip())  # Elimina espacios en blanco a la izquierda
print(animal.rstrip())  # Elimina espacios en blanco a la derecha
print(animal.find("CH"))  # Busca la posición de la primera coincidencia asi que devuelve un indice
print(animal.replace("chan", "Don_"))  # Reemplaza una cadena por otra
print("nCH" in animal)  # Busca una cadena dentro de otra pero devuelve un booleano
print("nCH" not in animal)  # Busca una cadena dentro de otra, pero devuelve un booleano negado (inverso)
