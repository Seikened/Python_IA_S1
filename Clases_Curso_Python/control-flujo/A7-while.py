comando = ""
while True:
	comando = input("Introduzca un comando: ")
	print("Ha escrito", comando)
	if comando.lower() == "salir":
		break
