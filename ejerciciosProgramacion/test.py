c_x = float(input("Ingrese la coordenada de X: "))
c_y = float(input("Ingrese la coordenada de Y: "))

x = (c_x - 2.5) // 15
y = (c_y - 2.5) // 15

userTornillo = (y * 8) + x  # 8

print(f"El tornillo es: {userTornillo}")
