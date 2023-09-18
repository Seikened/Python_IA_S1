c_x_mm = float(input("Ingrese la coordenada de X: "))
c_y_mm = float(input("Ingrese la coordenada de Y: "))
columna = c_x_mm // 15
renglon = c_y_mm // 15
# Despeje de n
n = (renglon * 8) + columna
resultado = int(n)

print(f"""Para la coordenana de columna: 🔹{c_x_mm}🔹 y las de renglon: 🔹{c_y_mm}🔹El tornillo buiscado es: {resultado}""")

