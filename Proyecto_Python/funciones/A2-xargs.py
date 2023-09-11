from ... / ejercicios / funcio


def suma(*numeros):
	resultado = 0
	for numero in numeros:
		resultado += numero
	resultado = resultado / len(numeros)
	return resultado


# preguntar el usuario cuantos números queire meter
entrada = int(input("¿Cuántos números quieres introducir? "))
numeros = []
for i in range(entrada):
	numeros.append(float(input("Introduce un número: ")))
print(suma(*numeros))
