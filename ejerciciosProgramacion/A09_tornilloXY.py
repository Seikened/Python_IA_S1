from A08_tornillo import calcularTornillo


def calcular_coordenadas_tornillo_corregido(numero_tornillo):
	distanciaConstante = 15
	renglon = numero_tornillo // 8
	columna = numero_tornillo % 8

	posicion_x = calcularTornillo(columna)
	posicion_y = calcularTornillo(renglon)

	return posicion_x, posicion_y


entradaUserTornillo = int(input("Ingrese la posicion del tornillo: "))
x, y = calcular_coordenadas_tornillo_corregido(entradaUserTornillo)
print(f"Para el tornillo 🔹{entradaUserTornillo}🔹 las coordenadas de X es: {x} | Y es: {y}")
