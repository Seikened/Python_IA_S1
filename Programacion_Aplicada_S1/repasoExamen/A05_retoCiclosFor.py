from math import inf


listaFlotante = []
tamLista = int(input("De que tamaño quieres tu lista: "))

for index in range(tamLista):
    numero = float(input("Introduce tu número: "))
    listaFlotante.append(numero)
    
print(listaFlotante)


numeroMayor = -inf
numeroMenor = inf
for numero in listaFlotante:
    if numero >numeroMayor:
        numeroMayor = numero
    
    if numero < numeroMenor:
        numeroMenor = numero

print(f"Número mayor es: {numeroMayor}, y el número menor es:{numeroMenor}")



# Promedio
sumatoriaPromedio = 0
for numero in listaFlotante:
    sumatoriaPromedio += numero

promedio = sumatoriaPromedio / len(listaFlotante)

print(f"Tu promedio es {promedio}")
