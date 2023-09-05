numero =  float(input("Ingrese un numero a redondear: "))
decimales = int(input("Ingrese la cantidad de decimales: "))

def redondear(numero, decimales=0):
	factor = 10 ** decimales # Aqui se toma que si busco 2 decimales, el factor es 100, si busco 3, el factor es 1000, etc.
	# El numero primero se multiplica para recorrer la coma la cantidad de decimales que se buscan,
	# luego se suma 0.5 para que el redondeo sea correcto y suba el numero si es necesario.
	calculo = (numero * factor) + 0.5
	# Se divide por los mismos decimales para que el numero vuelva a su estado original, pero redondeado.
	return int(calculo)/factor

print(f"Tu numero {numero} se ha redondeado a {decimales} decimales resultando: ",redondear(numero, decimales))