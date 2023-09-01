# def billetes(monto,valor_billete):
# 	cantidad_billetes = 0
# 	while (monto // valor_billete) != 0:
# 		cantidad_billetes += 1
# 		monto -= valor_billete
# 	return monto, cantidad_billetes
#
# monto = int(input("Ingrese el monto: "))
# monto_copia = monto
# monto, billete_1000 = billetes(monto,1000)
# monto, billete_500 = billetes(monto,500)
# monto, billete_200 = billetes(monto,200)
# monto, billete_100 = billetes(monto,100)
# monto, billeteQuinientos = billetes(monto, 50)
#
# if monto == 0:
# 	print("Se puede dar el monto exacto")
# 	print("Billetes de 1000: ", billete_1000)
# 	print("Billetes de 500: ", billete_500)
# 	print("Billetes de 200: ", billete_200)
# 	print("Billetes de 100: ", billete_100)
# 	print("Billetes de 50: ", billeteQuinientos)
# 	print("Monto: ", monto_copia)
# else:
# 	print("No se puede dar el monto exacto")
#


monto = 2250
monto_copia = monto

# Billetes de 1000
cantidad_billetes = 0 # Aqui se guarda la cantidad de billetes
operación = monto // 1000 # Aqui se divide el monto entre el valor del billete
cantidad_billetes += operación # Aqui se acumula la cantidad de billetes
monto -= 1000 * operación # Aqui se resta el monto con la cantidad de billetes
print("Billetes de 1000: ", cantidad_billetes) # Aqui se imprime la cantidad de billetes

# Billetes de 500
cantidad_billetes = 0
operación = monto // 500
cantidad_billetes += operación
monto -= 500 * operación
print("Billetes de 500: ", cantidad_billetes)

# Billetes de 200
cantidad_billetes = 0
operación = monto // 200
cantidad_billetes += operación
monto -= 200 * operación
print("Billetes de 200: ", cantidad_billetes)

# Billetes de 100
cantidad_billetes = 0
operación = monto // 100
cantidad_billetes += operación
monto -= 100 * operación
print("Billetes de 100: ", cantidad_billetes)

# Billetes de 50
cantidad_billetes = 0
operación = monto // 50
cantidad_billetes += operación
monto -= 50 * operación
print("Billetes de 50: ", cantidad_billetes)