numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero)
print(segundo)
print(otros)
for n in numeros:
	print(n)

listaNumeros = list(numeros)
listaNumeros[0] = "Hola"
print(listaNumeros)
