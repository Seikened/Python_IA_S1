indice = int(input("Dime el indice a descartar: "))
vector = [8,2,-1,5,14,6]


print(vector)

suma = 0
for posicion , numero in enumerate(vector):
    if posicion == indice:
        print(f"No se suma el {indice}")
    else:
        suma += numero

print(f"La suma total es: {suma}")
