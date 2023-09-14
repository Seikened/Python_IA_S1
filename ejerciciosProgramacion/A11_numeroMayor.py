def numeroMayor(primerValor, segundoValor):
	valormayor = primerValor
	if primerValor > valormayor:
		valormayor = primerValor
	if segundoValor > valormayor:
		valormayor = segundoValor
	return valormayor


if __name__ == "__main__":
	primerValor = float(input("Ingresa el primer valor: "))
	segundoValor = float(input("Ingresa el segundo valor: "))
	print(f"El valor mayor es {numeroMayor(primerValor, segundoValor)}")