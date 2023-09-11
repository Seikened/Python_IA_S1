def palindromo(palabra):
	palabraDerecho = palabra.lower()
	palabraRevez = []
	palabraComparar=[]
	# Ordeno las palabras
	for char in palabraDerecho:
		if char != " ":
			palabraRevez.append(char)
	palabraComparar = palabraRevez[::-1]
	sentencia = True if palabraRevez == palabraComparar else False
	return sentencia


palabraUser = input("Ingrese una palabra: ")
print(f"La palabra {palabraUser} es palindromo" if palindromo(palabraUser) else f"La palabra {palabraUser} no es palindromo")