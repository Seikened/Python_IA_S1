from math import comb


def calcular_probabilidad_binomial():
	# Solicitar las variables del usuario
	experimento = int(input("Introduce el número total de ensayos (n): "))
	probabilidadDelEnsayo = float(input("Introduce la probabilidad de éxito en un solo ensayo (p): "))
	exitos = int(input("Introduce el número de éxitos que estás buscando (E): "))

	coef_binomial = comb(experimento, exitos)

	probabilidad = coef_binomial * (probabilidadDelEnsayo ** exitos) * (
			(1 - probabilidadDelEnsayo) ** (experimento - exitos))

	print(f"La probabilidad de tener exactamente {exitos} éxitos en {experimento} ensayos es: {probabilidad:.6f}")


calcular_probabilidad_binomial()
# Fax es Exito
# A) P(X>=6) 25
# B) P(x = 6) La probabilidad de tener exactamente 6 éxitos en 25 ensayos es: 0.182820
# C) P(x<=6) La probabilidad acumulada de tener 6 o menos éxitos en 25 ensayos es: 0.561098
# D) P(x>6)
