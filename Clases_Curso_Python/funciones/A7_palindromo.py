def palindromo(palabra):
	palabraDerecho = palabra.lower()
	palabraRevez = []
	palabraComparar = []
	# Ordeno las palabras
	for char in palabraDerecho:
		if char != " ":
			palabraRevez.append(char)
	palabraComparar = palabraRevez[::-1]
	sentencia = True if palabraRevez == palabraComparar else False
	return sentencia


palabraUser = input("Ingrese una palabra: ")
print(f"La palabra {palabraUser} es palindromo" if palindromo(
	palabraUser) else f"La palabra {palabraUser} no es palindromo")

# def es_palindromo(palabra):
#     palabra = palabra.lower().replace(" ", "")
#     return palabra == palabra[::-1]
#
# palabra_usuario = input("Ingrese una palabra o frase para verificar si es un palíndromo: ").lower()
# resultado = "es un palíndromo" if es_palindromo(palabra_usuario) else "no es un palíndromo"
#
# print(f"La palabra o frase '{palabra_usuario}' {resultado}.")
