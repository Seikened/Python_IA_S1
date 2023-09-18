# Función para calcular x y y en función de c
def calcular_xy(c_x, c_y):
	x = (c_x - 2.5) // 15
	y = (c_y - 2.5) // 15
	# Despeje de n
	n = (y * 8) + x
	print(f"El numero a obtener es: {n}")
	return n


if __name__ == "__main__":
	# Coordenadas introducidas por el usuario para x y y
	c_x = float(input("Ingrese la coordenada de X: "))
	c_y = float(input("Ingrese la coordenada de Y: "))

	# Calculamos x y y
	resultado = calcular_xy(c_x, c_y)

	print(f"""
    Para la coordenana de X: 🔹{c_x}🔹 y las de Y: 🔹{c_y}🔹
    las coordenadas de es: {resultado}

    """)
