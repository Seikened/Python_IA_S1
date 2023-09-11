def factorial(numero):
	factorial = 1
	for i in range(1, numero + 1):
		factorial = factorial * i
	return factorial


def distribucionPoisson(lambdaVariable, numeroOcurrencias):
	euler = 2.7182818284590452353602874713527
	distribucionPoisson = ((lambdaVariable ** numeroOcurrencias) * (euler ** (-lambdaVariable))) / factorial(
		numeroOcurrencias)
	return distribucionPoisson


lambdaUser = float(input("Ingrese el valor de lambda: "))
numeroOcurrenciasUser = int(input("Ingrese el valor de numero de ocurrencias: "))

if __name__ == '__main__':
	print(f"La distribucion de poisson es: {distribucionPoisson(lambdaUser, numeroOcurrenciasUser)}")
