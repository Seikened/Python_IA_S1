a = [[1, 0, -1, 1],
     [2, 1, -3, 4],
     [-2, 1, 4, 6],
     [0, 2, 3, 5]]

b = [[2, 4, 1, 6],
     [3, 0, -2, 5],
     [2, 1, -1, 0],
     [-2, -4, 1, 3]]

c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(a[0])):
			posicionA = a[i][k]
			posisionB = b[k][j]
			c[i][j] += posicionA * posisionB
	print(f"valor de iteración  y {c}")
