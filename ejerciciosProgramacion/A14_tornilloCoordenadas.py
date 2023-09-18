# Función para calcular x y y en función de c
def calcular_xy(c_x_mm, c_y_mm):
	x = (c_x_mm - 2.5) // 15
	y = (c_y_mm - 2.5) // 15
	# Despeje de n
	n = (y * 8) + x
	return n


if __name__ == "__main__":
	# Coordenadas introducidas por el usuario para x y y
	c_x_mm = float(input("Ingrese la coordenada de X: "))
	c_y_mm = float(input("Ingrese la coordenada de Y: "))

	# Calculamos x y y
	resultado = int(calcular_xy(c_x_mm, c_y_mm))

	print(f"""Para la coordenana de X: 🔹{c_x_mm}🔹 y las de Y: 🔹{c_y_mm}🔹
El tornillo buiscado es: {resultado}
""")
