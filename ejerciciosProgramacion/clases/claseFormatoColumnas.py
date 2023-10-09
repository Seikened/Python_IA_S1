import random


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
La mecánica es que ocupas poner un número 
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
	sumaApuesta = -1
	while sumaApuesta < 2 or sumaApuesta > 12:
		sumaApuesta = int(input("Ingrese un número entre 2 y 12: "))

	if sumaApuesta == sumaDados:
		creditoInicial += montoApuesta
		print(f"En hora buena le haz atinado🎉")
		if montoApuesta != 0:
			print(f"Obtuviste🎉 ${montoApuesta}")
	else:
		creditoInicial -= montoApuesta
		print(f"Oh rayos 🥺 no le acertaste, salio {sumaDados}")
		if montoApuesta != 0:
			print(f"Perdiste🎉 ${montoApuesta}")
		if creditoInicial == 0:
			print("Ya no tienes más créditos para jugar 🚫")
			break

	print(f"Tu crédito es ${creditoInicial}")
	respuesta = input("¿Desea seguir jugando? (s/n): ").lower()
	if respuesta == "n":
		break

	montoApuesta = float(input("Ingrese su apuesta: "))
	while montoApuesta < 0 or montoApuesta > creditoInicial:
		montoApuesta = int(input(f"Ingresa un valor entre 0 y {creditoInicial}: "))

print("Fin del juego")
