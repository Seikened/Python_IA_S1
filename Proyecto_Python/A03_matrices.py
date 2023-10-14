import random

def numeroMatriz():
     numero = random.randint(-10,10)
     return numero

while True:
     # Matríz a
     columnasA =  int(input("Cuantas colunmas de la matríz a: "))
     renglonesA =  int(input("Cuantos renglones de la matríz a: "))
     # Matríz b
     columnasB = int(input("Cuantas colunmas de la matríz b: "))
     renglonesB = int(input("Cuantos renglones de la matríz b: "))
     if columnasA == renglonesB:
          break

a = [[numeroMatriz() for _ in range(columnasA)] for _ in range(renglonesA)]
print(f"MATRÍZ A: \n{a}\n")

b = [[numeroMatriz() for _ in range(columnasB)] for _ in range(renglonesB)]
print(f"MATRÍZ B: \n{b}\n")
     

lista = [[] ]

# Tamaño de la matríz c
c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(a[0])):
			posicionA = a[i][k]
			posisionB = b[k][j]
			c[i][j] += posicionA * posisionB

print(F"MATRÍZ RESULTANTE: \n{c}")
