import random

def numeroAleatorio():
    return random.randint(1,10)
    
    
lista = [numeroAleatorio() for _ in range(10)]

suma = 0
for numero in lista:
    suma += numero
media = suma / len(lista)


sumaCuadrados = 0
for numero in lista:
    sumaCuadrados += (numero - media)**2 

distribucionEstandarPoblacion = (sumaCuadrados/len(lista))**(0.5)

print(f"La distribución estándar de {lista} es: {distribucionEstandarPoblacion}")