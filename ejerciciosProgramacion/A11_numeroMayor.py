# Version: 1.0
primerValor = float(input("Ingresa el primer valor: "))
segundoValor = float(input("Ingresa el segundo valor: "))

if primerValor > segundoValor:
	print(f"El primer valor es mayor {primerValor}")
elif segundoValor > primerValor:
	print(f"El segundo valor es mas grande {segundoValor}")
else:
	print(f"Son iguales el primer valor {primerValor} y el segudo valor {segundoValor}")