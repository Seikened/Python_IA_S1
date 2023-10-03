# 1.- Escriba un programa que escriba las siguientes secuencias de valores.
# Para cada secuencia de valores use un ciclo while diferente.
# No es necesario que los valores aparezcan en el mismo renglón ni separados por comas.
# Puede ser como en el ejemplo de arriba.

# a) 1,2,3,4,5,6,7
# b) 3,8,13,18,23
# c) 20,14,8,2,-4,-10
# d) 19,27,35,43,51

# While ------------------------------------------------------------

# a)
i = 1
while (i < 8):
	print(f"Valor de incremento {i}")
	i += 1
print("Fin secuencia de while incremento de 1 en 1 iniciando de 1")

# b)
i = 3
while (i < 24):
	print(f"Valor de incremento {i}")
	i += 5
print("Fin secuencia de while incremento de 5 en 5 iniciando de 3")

# c)
i = 20
while (i > -11):
	print(f"Valor de incremento {i}")
	i -= 6
print("Fin secuencia de while decremento de 6 en 6 iniciando de 20")

# d)
i = 19
while (i < 52):
	print(f"Valor de incremento {i}")
	i += 8
print("Fin secuencia de while incremento de 8 en 8 iniciando de 19")
