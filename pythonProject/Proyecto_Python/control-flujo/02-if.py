edad = 56

if edad > 54:
	print("🎫Recibes un descuento para ver tu pelicula")
elif edad >= 18:
	print("✅Puedes ver la pelicula")
else:
	print("❌No puede ver la pelicula")


if edad >= 18:
	if edad > 54:
		print("🎫Recibes un descuento para ver tu pelicula")
	else:
		print("✅Puedes ver la pelicula eres mayor")
else:
	print("❌No puede ver la pelicula")