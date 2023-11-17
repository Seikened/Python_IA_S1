# # Clone de una variable
# x = 50
# y = x # Y es un clon de X por que en realidad apuntan a la misma direccion de memoria
# y = 100

# print(f"X: {x}")
# print(f"Y: {y}")


# # Alias de una variable

# x = [10, 20, 30]
# y = x # Y es un alias de X por que en realidad apuntan a la misma direccion de memoria
# y[0] = 100

# print(f"LISTA X: {x}")
# print(f"LISTA Y: {y}")

# #----------------------------------------------------------------------------------------------------

# # Ahora vamos a hacer un clone de una lista

# x = [10, "JAJAJA", "tE DIJE"]
# y = x[:]  # Esto es un clone de la lista X pero NO ES la misma direccion de memoria
# y[0] = "Hola fui cloanda"

# print(f"LISTA X: {x}")
# print(f"LISTA CLONADA Y: {y}")


# calificaciones = [10,9.4, 8.2, 5.6, 7.8, 9.1, 10, 8.9, 7.7, 6.6, 5.5, 4.4, 3.3, 2.2, 1.1]

# calificaciones.sort()

# medio = len(calificaciones) // 2

# mediana = calificaciones[medio]
# print(f"La mediana es: {mediana}")


# Estructura de datos

# nombre = "Juan"
# credito = 1000
# sumaApuesta = 7
# montoApuesta =  150

# jugadorUno = [nombre,credito,sumaApuesta,montoApuesta]

# print(jugadorUno)

# nombre = "Pedro"
# credito = 500
# sumaApuesta = 4
# montoApuesta =  250

# jugadorDos = 

# print(jugadorDos)



# mesaJugadores = [jugadorUno, jugadorDos]


# print(mesaJugadores)


numeroJugadores = int(input("Cuantos jugadores son: "))
mesaJugadores = []


import random
#f"Jugador {numeroJugador}"
for numeroJugador in range(numeroJugadores):
    nombre = input("Cual es tu nombre")
    credito = random.randint(1,250)
    sumaApuesta = random.randint(1,15)
    montoApuesta = random.randint(1,250)
    jugador = [nombre,credito,sumaApuesta,montoApuesta]
    mesaJugadores.append(jugador)
    

mayorCaracteres = 0
for index in range(len(mesaJugadores)):
    esteJuagador = mesaJugadores[index]
    nombre = esteJuagador[0]
    credito = esteJuagador[1]
    sumaApuesta = esteJuagador[2]
    montoApuesta = esteJuagador[3]
    
    if len(nombre) > mayorCaracteres:
        mayorCaracteres = len(nombre)
    
for esteJugador in mesaJugadores:
    nombre, credito, sumaApuesta, montoApuesta = esteJugador
    print(f"{nombre:<{mayorCaracteres}} {credito:<10} {sumaApuesta:<15} {montoApuesta:<15}")