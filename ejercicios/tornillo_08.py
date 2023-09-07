def calcularTornillo(posicion, distanciaConstante=15):
	posicion = (posicion*distanciaConstante) + 7.5
	return posicion
entrada = int(input("Ingrese la posicion del tornillo: "))
if __name__ == "__main__":

    print(f"La posicion del tornillo es: {calcularTornillo(entrada)}")