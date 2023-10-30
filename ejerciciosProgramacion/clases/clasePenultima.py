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



# for numeroJugador in range(numeroJugadores):
#     nombre = str(input("Cual es tu nombre: "))
#     credito = int(input("Que crédito tiene: "))
#     sumaApuesta = int(input("Que numero es al que le apuestas: "))
#     montoApuesta = int(input("Cual es el monto que aúestas: "))
#     jugador = [nombre,credito,sumaApuesta,montoApuesta]
#     mesaJugadores.append(jugador)

# print(mesaJugadores)
import random

for numeroJugador in range(numeroJugadores):
    nombre = f"Jugador {numeroJugador}"
    credito = random.randint(1,250)
    sumaApuesta = random.randint(1,15)
    montoApuesta = random.randint(1,250)
    jugador = [nombre,credito,sumaApuesta,montoApuesta]
    mesaJugadores.append(jugador)

print(mesaJugadores)