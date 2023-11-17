def numeroPar(numero):
	if numero % 2 == 0:
		print("El numero es par")
	else:
		print("El numero es impar")


if __name__ == "__main__":
	numero = int(input("Ingrese un numero: "))
	numeroPar(numero)
