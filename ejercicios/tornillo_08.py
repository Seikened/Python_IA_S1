def calcularTornillo(posicion, distanciaConstante=15):
	posicion = (posicion*distanciaConstante) + 7.5
	return posicion

if __name__ == "__main__":
    print(f"La posicion del tornillo es: {calcularTornillo(6)}")