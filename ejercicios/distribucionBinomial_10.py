from math import comb


def calcular_probabilidad_binomial():
	# Solicitar las variables del usuario
	n = int(input("Introduce el número total de ensayos (n): "))
	p = float(input("Introduce la probabilidad de éxito en un solo ensayo (p): "))
	E = int(input("Introduce el número de éxitos que estás buscando (E): "))

	coef_binomial = comb(n, E)

	probabilidad = coef_binomial * (p ** E) * ((1 - p) ** (n - E))

	print(f"La probabilidad de tener exactamente {E} éxitos en {n} ensayos es: {probabilidad:.6f}")

calcular_probabilidad_binomial()
# Fax es Exito
# A) P(X>=6) 25
# B) P(x = 6) La probabilidad de tener exactamente 6 éxitos en 25 ensayos es: 0.182820
# C) P(x<=6) La probabilidad acumulada de tener 6 o menos éxitos en 25 ensayos es: 0.561098
# D) P(x>6)