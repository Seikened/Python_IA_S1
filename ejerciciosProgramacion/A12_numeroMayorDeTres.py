a = float(input("Escribe el primer número: "))
b = float(input("Escribe el segundo número: "))
c = float(input("Escribe el tercero número: "))
numeroMayor = a

if b >numeroMayor:
	numeroMayor = b
if c>numeroMayor:
	numeroMayor = c


print(f"El número mayor es {numeroMayor}")