#Simulación de baraja
import random


lista = []

for i in range(1, 7):
    lista.append(i)

print("Lista original: ", lista)

for i in range(6):
    for posicion in range(0,6):
        nuevaPosicion = random.randint(0,5)
        
        (lista[posicion],lista[nuevaPosicion]) = (lista[nuevaPosicion],lista[posicion])
        
    print("Lista revuelta", lista)
    
    
lista = [1,2,3,4,5,6,7,8,9,10]
nuevaLista = random.shuffle(lista)
print(lista)