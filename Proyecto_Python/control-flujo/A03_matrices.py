a = [[2, 16],
     [3, 11]]
b = [[2, 16],
     [3, 11]]
c = 0
i = 0
j = 0

for i in range(len([j])):
	c = 0
	for k in range(len(a[i])):
		posicionA = a[i][k]
		posisionB = b[k][i]
		print(f" Posicion a: {posicionA} posicion b: {posisionB}")
		c += posicionA * posisionB
		print(f"Resultado de c: {c}")
	print(f"valor de iteración {i} y {c}")
