# Busqueda exahustiva

# resolver x para x**3+x = 100
# print("      x     |    Lado Izq.")
# print("------------|----------------")
# x = 4
# ladoDer = 100
# ladoIzquierdo = x ** 3 + x
# while (ladoIzquierdo < ladoDer):
# 	ladoIzquierdo = x ** 3 + x
# 	print(" %10.5f | %10.5f" % (x, ladoIzquierdo))
# 	x += .00001


# Casino
# Tener credito inicial
# Apostar
# Si gana, se le suma el doble de lo apostado
# Si pierde, se le resta lo apostado
# Si se queda sin credito, se le da la opcion de salir
# Puede salir en cualquier momento

# Primero tengo que generar dados
# Segundo preguntar por el número  e indentificar si gana o pierde
# Tercero preguntar si quiere seguir jugando
# Cuarto Voy a agregar el crédito y apuestas
# cuatro punto 1: Aqui hay varias reglas de casino y reglas de juego

import random

# Primero tengo que generar dados
respuesta = "s"
while respuesta == "s":
	dadoUno = random.randint(1, 6)
	dadoDos = random.randint(1, 6)
	print(f"Dado uno: {dadoUno} y Dado dos: {dadoDos}")
	creditoInicial = 100

	# Segundo preguntar por el número  e indentificar si gana o pierde
	sumaApuesta = int(input("Ingrese un número entre 2 y 12: "))
	sumaDados = dadoUno + dadoDos
	if sumaApuesta == sumaDados:
		print("Ganaste")
		respuesta = input("¿Desea seguir jugando? (s/n): ")
		apuesta = int(input("Ingrese su apuesta: "))
	else:
		print("Perdiste")
		respuesta = input("¿Desea seguir jugando? (s/n): ")
		apuesta = int(input("Ingrese su apuesta: "))  # esto sirve para que el usuario pueda apostar de nuevo

# no puedes apoar mas de lo que tienes
# si ya no tienes dinero te tienes que salir del casino
# Jugador tiene que tener la opcion de salir en cualquier momento
