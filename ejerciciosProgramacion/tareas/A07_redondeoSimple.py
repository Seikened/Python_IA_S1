def redondear(numero, decimales=0):
	factor = 10 ** decimales
	# Aqui se toma que si busco 2 decimales, el factor es 100, si busco 3, el factor es 1000, etc.
	# El numero primero se multiplica para recorrer la coma la cantidad de decimales que se buscan,
	# luego se suma 0.5 para que el redondeo sea correcto y suba el numero si es necesario.
	calculo = (numero * factor) + 0.5
	# Se divide por los mismes decimales para que el numero vuelva a su estado original, pero redondeado.
	return int(calculo) / factor


# Redondeo simple de:
# 9.43 -> 9.4
# 9.56 -> 9.6
# 9.99 -> 10.0
# 9.93 -> 9.9
print(f"El redondeo de 9.43 es: {redondear(9.43, 1)}")
print(f"El redondeo de 9.56 es: {redondear(9.56, 1)}")
print(f"El redondeo de 9.99 es: {redondear(9.99, 1)}")
print(f"El redondeo de 9.93 es: {redondear(9.93, 1)}")
