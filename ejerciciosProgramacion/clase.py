edad = int(input("Introduce tu edad: "))
permisoTutor = input("¿Tienes permiso de tus padres? (si/no): ")

if (edad >= 18) or (edad >= 16 and permisoTutor == "si"):
	print("Puedes tramitar tu licencia")
	print("Toma foto, hacer examen médico, pagar y tramitar tu licencia")
else:
	print("No puedes tramitar tu licencia")
	print("Debes tener 18 años o más o 16 con permiso de tus padres")
print("Fin del programa")
