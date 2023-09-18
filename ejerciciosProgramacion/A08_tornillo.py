def calcularTornillo(entradaTornillo, distanciaConstante=15):
	x_mm = (entradaTornillo * distanciaConstante) + 7.5
	return x_mm


entradaTornillo = int(input("Ingrese la posicion del tornillo: "))
if __name__ == "__main__":
	print(f"La posicion del tornillo es: {calcularTornillo(entradaTornillo)}")
