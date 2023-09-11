saludo = "Hola global"

def hola():
	global saludo
	saludo = "Hola Mundo"

def saludaChanchito():
	saludo = "Hola Chanchito"



print(saludo)
hola()
print(saludo)