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


# Nueva función para calcular la probabilidad acumulada en la distribución de Poisson
def distribucionPoissonAcumulada(lambdaVariable, max_numeroOcurrencias):
	probabilidad_acumulada = 0.0
	for i in range(max_numeroOcurrencias + 1):  # Sumamos desde 0 hasta max_numeroOcurrencias
		probabilidad_acumulada += distribucionPoisson(lambdaVariable, i)
	return probabilidad_acumulada


if __name__ == '__main__':
	lambdaUser = float(input("Ingrese el valor de lambda: "))
	numeroOcurrenciasUser = int(input("Ingrese el valor de numero maximo de ocurrencias: "))
	print(f"La probabilidad acumulada de Poisson es: {distribucionPoissonAcumulada(lambdaUser, numeroOcurrenciasUser)}")
