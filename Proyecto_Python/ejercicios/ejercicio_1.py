def billetes(monto,valor_billete):
	cantidad_billetes = 0
	while (monto // valor_billete) != 0:
		cantidad_billetes += 1
		monto -= valor_billete
	return monto, cantidad_billetes

monto = int(input("Ingrese el monto: "))
monto_copia = monto
monto, billete_1000 = billetes(monto,1000)
monto, billete_500 = billetes(monto,500)
monto, billete_200 = billetes(monto,200)
monto, billete_100 = billetes(monto,100)
monto, billeteQuinientos = billetes(monto, 50)

if monto == 0:
	print("Se puede dar el monto exacto")
	print("Billetes de 1000: ", billete_1000)
	print("Billetes de 500: ", billete_500)
	print("Billetes de 200: ", billete_200)
	print("Billetes de 100: ", billete_100)
	print("Billetes de 50: ", billeteQuinientos)
	print("Monto: ", monto_copia)
else:
	print("No se puede dar el monto exacto")

