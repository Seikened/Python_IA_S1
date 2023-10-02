# Busqueda exahustiva

# resolver x para x**3+x = 100

x = 4
while (x < 5):
	ladoIzquierdo = x ** 3 + x
	print("x: %10.4f, Lado izquierdo: %10.4f" % (x, ladoIzquierdo))
	x += .01
