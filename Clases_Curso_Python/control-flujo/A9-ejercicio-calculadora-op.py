print("Bienvenido a la calculadora de operaciones")
print("Para salir del programa escriba 'salir'")
print("Las operaiones disponibles son: suma, resta, multiplicacion y division")
# primerNumero = input("Ingrese el primer numero: ")
# operacion = primerNumero
# while operacion.lower() != "salir":
# 	operacion = primerNumero
# 	operacion = input("Ingrese la operacion: ")
# 	segundoNumero = input("Ingrese el segundo numero: ")
# 	if operacion.lower() == "suma":
# 		resultado = int(primerNumero) + int(segundoNumero)
# 		print(f"El resultado de la suma de {primerNumero} con {segundoNumero} es: {resultado}")
# 		primerNumero = resultado
# 	elif operacion.lower() == "resta":
# 		resultado = int(primerNumero) - int(segundoNumero)
# 		print(f"El resultado de la resta de {primerNumero} con {segundoNumero} es: {resultado}")
# 		primerNumero = resultado
# 	elif operacion.lower() == "multiplicacion":
# 		resultado = int(primerNumero) * int(segundoNumero)
# 		print(f"El resultado de la multiplicacion de {primerNumero} con {segundoNumero} es: {resultado}")
# 		primerNumero = resultado
# 	elif operacion.lower() == "division":
# 		resultado = int(primerNumero) / int(segundoNumero)
# 		print(f"El resultado de la division de {primerNumero} con {segundoNumero} es: {resultado}")
# 		primerNumero = resultado
# 	else:
# 		print("Operacion no valida")
# 		operacion = primerNumero
# 		operacion = input("Ingrese la operacion correctamente: ")
# 		segundoNumero = input("Ingrese el segundo numero: ")
# 		if operacion.lower() == "suma":
# 			resultado = int(primerNumero) + int(segundoNumero)
# 			print(f"El resultado de la suma de {primerNumero} con {segundoNumero} es: {resultado}")
# 			primerNumero = resultado
# 		elif operacion.lower() == "resta":
# 			resultado = int(primerNumero) - int(segundoNumero)
# 			print(f"El resultado de la resta de {primerNumero} con {segundoNumero} es: {resultado}")
# 			primerNumero = resultado
# 		elif operacion.lower() == "multiplicacion":
# 			resultado = int(primerNumero) * int(segundoNumero)
# 			print(f"El resultado de la multiplicacion de {primerNumero} con {segundoNumero} es: {resultado}")
# 			primerNumero = resultado
# 		elif operacion.lower() == "division":
# 			resultado = int(primerNumero) / int(segundoNumero)
# 			print(f"El resultado de la division de {primerNumero} con {segundoNumero} es: {resultado}")
# 			primerNumero = resultado
# 		else:
# 			print("Operacion no valida se cerrara el programa")
# 			operacion = "salir"

resultado = ""
while True:
	if not resultado:
		resultado = input("Ingrese el primer numero: ")
		if resultado.lower() == "salir":
			break
		resultado = int(resultado)
	operacion = input("Ingrese la operacion: ")
	if operacion.lower() == "salir":
		break
	segundoNúmero = input("Ingresa segundo número: ")
	if segundoNúmero.lower() == "salir":
		break
	segundoNúmero = int(segundoNúmero)
	if operacion == "suma":
		resultado += segundoNúmero
	elif operacion == "resta":
		resultado -= segundoNúmero
	elif operacion == "division":
		operacion /= segundoNúmero
	elif operacion == "multi":
		operacion *= segundoNúmero
