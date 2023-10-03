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
montoApuesta = 0
creditoInicial = 100
print(f"""
Bienvenido al casino!
Tendrás un primer tiro de prueba para que te 
familiarices con el juego.

Tu crédito inicial es: {creditoInicial}
Y tu monto de apuesta es: {montoApuesta} 
esta en 0 por que aun no haz apostado.

Después de tu primer tiro empezarás a apostar
-------------------------------------------------
La mecanica es que ocupas poner un número 
Entre 2 y 12 y si aciertas se sumara el monto de tu apuesta a tu crédito

""")

respuesta = "s"
while respuesta == "s":

	if creditoInicial == 0:
		print("Ya no tienes más créditos para jugar 🚫")
		break

	dadoUno = random.randint(1, 6)
	dadoDos = random.randint(1, 6)
	sumaDados = dadoUno + dadoDos

	print(f"Dado uno: {dadoUno} y Dado dos: {dadoDos} el resultado es {sumaDados}")
	sumaApuesta = int(input("Ingrese un número entre 2 y 12: "))


	if sumaApuesta == sumaDados:
		creditoInicial += montoApuesta
		print(f"En hora buena le haz atinado🎉")
		if montoApuesta != 0:
			print(f"Obtuviste🎉 {montoApuesta} y tienes {creditoInicial} créditos acumulados")
	else:
		creditoInicial -= montoApuesta
		print(f"Oh rayos 🥺 no le acertaste")
		if montoApuesta != 0:
			print(f"Perdiste🎉 {montoApuesta} y tienes {creditoInicial} créditos acumulados")
		if creditoInicial == 0:
			print("Ya no tienes más créditos para jugar 🚫")
			break


	respuesta = input("¿Desea seguir jugando? (s/n): ").lower()

	montoApuesta = int(input("Ingrese su apuesta: "))
	while montoApuesta > creditoInicial:
		montoApuesta = int(input(f"Ingresa un valor mejor a {creditoInicial}: "))

print("Fin del juego")
