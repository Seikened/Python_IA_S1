# and or not

# Auto

gas = True
encendido = True
edad = 23
licencia = True

# if not (edad >= 18):
# 	mensaje = "No puedes conducir, no eres mayor de edad"
# elif not gas or not encendido:
# 	mensaje = "El auto no puede ser usado, verifica que tenga gasolina y este encendido"
# else:
# 	mensaje = "A MANEJAR!!!" if licencia else "No puedes conducir, no tienes licencia"
#
# print(mensaje)


if not gas and encendido and edad > 17:
	mensaje = "A MANEJAR!!!"
