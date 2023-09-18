numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Esto es muy tedioso y feo de hacer
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, *otros, ultimo = numeros

print(primero)
print(otros)
print(ultimo)
