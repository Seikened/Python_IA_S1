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



monto = 2250


# Billetes de 500
cantidad_billetes = 0 # Crear una variable en cero
operación = monto // 500 # Verifico que mi monto se pueda dividir exacatamente entre los 500 pesos
cantidad_billetes += operación # Aquí lo que hago es sumar la cantidad de billetes a mi variable cantidad_billetes
monto -= 500 * operación
print("Billetes de 500: ", cantidad_billetes)

# Billetes de 250
cantidad_billetes = 0
operación = monto // 250
cantidad_billetes += operación
monto -= 250 * operación
print("Billetes de 250: ", cantidad_billetes)

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