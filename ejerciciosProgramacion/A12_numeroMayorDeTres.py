def numeroMayorDeTres(a, b, c):
	numeroMayor = a
	if b > numeroMayor:
		numeroMayor = b
	if c > numeroMayor:
		numeroMayor = c
	return numeroMayor


if __name__ == "__main__":
	a = float(input("Escribe el primer número: "))
	b = float(input("Escribe el segundo número: "))
	c = float(input("Escribe el tercero número: "))
	print(f"El número mayor es {numeroMayorDeTres(a, b, c)}")
