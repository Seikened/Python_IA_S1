# Busqueda exahustiva

# resolver x para x**3+x = 100
print("      x     |    Lado Izq.")
print("------------|----------------")
x = 4
ladoDer = 100
ladoIzquierdo = x ** 3 + x
while (ladoIzquierdo < ladoDer):
	ladoIzquierdo = x ** 3 + x
	print(" %10.5f | %10.5f" % (x, ladoIzquierdo))
	x += .00001
