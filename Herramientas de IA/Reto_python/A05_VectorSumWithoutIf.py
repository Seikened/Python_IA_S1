indice = int(input("Dime el indice a descartar: "))
vector = [8,2,-1,5,14,6]
sumaTotal = 0


for posicion , numero in enumerate(vector):
    sumaTotal += numero * (posicion!=indice)
    

print(f"La suma total es: {sumaTotal}")

