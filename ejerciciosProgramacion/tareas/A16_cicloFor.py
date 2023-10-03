# 1.- Escriba un programa que escriba las siguientes secuencias de valores.
# Para cada secuencia de valores use un ciclo while diferente.
# No es necesario que los valores aparezcan en el mismo renglón ni separados por comas.
# Puede ser como en el ejemplo de arriba.

# a) 1,2,3,4,5,6,7
# b) 3,8,13,18,23
# c) 20,14,8,2,-4,-10
# d) 19,27,35,43,51

# For ------------------------------------------------------------
# a)
for i in range(1, 8, 1):
	print(f"Valor de incremento {i}")
print("Fin secuencia de for incremento de 1 en 1 iniciando de 1")

# b)
for i in range(3, 24, 5):
	print(f"Valor de incremento {i}")
print("Fin secuencia de for incremento de 5 en 5 iniciando de 3")

# c)
for i in range(20, -11, -6):
	print(f"Valor de incremento {i}")
print("Fin secuencia de for decremento de 6 en 6 iniciando de 20")

# d)
for i in range(19, 52, 8):
	print(f"Valor de incremento {i}")
print("Fin secuencia de for incremento de 8 en 8 iniciando de 19")
