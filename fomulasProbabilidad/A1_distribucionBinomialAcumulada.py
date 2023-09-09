from math import comb


def calcular_probabilidad_acumulada_binomial(n, p, k):
	probabilidad_acumulada = 0.0

	for i in range(k + 1):
		coef_binomial = comb(n, i)
		probabilidad_i = coef_binomial * (p ** i) * ((1 - p) ** (n - i))
		probabilidad_acumulada += probabilidad_i

	return probabilidad_acumulada


def calcular_probabilidad_acumulada_binomial_usuario():
	n = int(input("Introduce el número total de ensayos (n): "))
	p = float(input("Introduce la probabilidad de éxito en un solo ensayo (p): "))
	k = int(input("Introduce el número máximo de éxitos que estás buscando (k): "))

	probabilidad_acumulada = calcular_probabilidad_acumulada_binomial(n, p, k)
	print(f"La probabilidad acumulada de tener {k} o menos éxitos en {n} ensayos es: {probabilidad_acumulada:.6f}")


calcular_probabilidad_acumulada_binomial_usuario()
