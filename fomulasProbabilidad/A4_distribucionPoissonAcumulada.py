from A3_distribucionPoisson import distribucionPoisson

# Nueva función para calcular la probabilidad acumulada en la distribución de Poisson
def distribucionPoissonAcumulada(lambdaVariable, max_numeroOcurrencias):
	probabilidad_acumulada = 0.0
	for i in range(max_numeroOcurrencias + 1):  # Sumamos desde 0 hasta max_numeroOcurrencias
		probabilidad_acumulada += distribucionPoisson(lambdaVariable, i)
	return probabilidad_acumulada


if __name__ == '__main__':

	tipoFuncion = input('Ingrese el tipo de funcion "Directa" o "Acumulada" ingresa [D] ó [A]: ').upper()
	if tipoFuncion == 'D':
		lambdaUser = float(input("Ingrese el valor de lambda: "))
		numeroOcurrenciasUser = int(input("Ingrese el valor de numero de ocurrencias: "))
		print(f"La probabilidad de Poisson es: {distribucionPoisson(lambdaUser, numeroOcurrenciasUser)}")
	elif tipoFuncion == 'A':
		lambdaUser = float(input("Ingrese el valor de lambda: "))
		numeroOcurrenciasUser = int(input("Ingrese el valor máximo de numero de ocurrencias: "))
		print(f"La probabilidad acumulada de Poisson es: {distribucionPoissonAcumulada(lambdaUser, numeroOcurrenciasUser)}")
