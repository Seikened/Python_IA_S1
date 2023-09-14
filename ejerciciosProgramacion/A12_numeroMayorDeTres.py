def numeroMayorDeTres(*numeros):
	numeroMayor = numeros[0]
	for numero in numeros:
		if numero > numeroMayor:
			numeroMayor = numero
	return numeroMayor


if __name__ == "__main__":
	cantidadNumerosIntroducir = int(input("Introduce la cantidad de números que quieres introducir: "))
	numeros = []
	for i in range(cantidadNumerosIntroducir):
		numero = int(input("Introduce un número: "))
		numeros.append(numero)
	print("El número mayor es: ", numeroMayorDeTres(*numeros))

