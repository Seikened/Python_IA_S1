def numeroMayorDeTres(*numeros):
	numeroMayor = numeros[0]
	for numero in numeros:
		if numero > numeroMayor:
			numeroMayor = numero
	return numeroMayor


if __name__ == "__main__": # para que no se me confundan chavos esto es
						#    solo para comprbar que el programa funcione cuando se ejecute este archivo

	cantidadNumerosIntroducir = int(input("Introduce la cantidad de números que quieres introducir: "))
	numeros = []
	for i in range(cantidadNumerosIntroducir):
		numero = float(input("Introduce un número: "))
		numeros.append(numero)
	print(f"El número mayor es: {numeroMayorDeTres(*numeros)}")

#  Esto es se debe hacer es:
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mayor = max(numeros)
# menor = min(numeros)
# promedio = sum(numeros) / len(numeros)
# print(mayor)