buscar_id = 2
for numero in range(5):
	print(numero)
	if numero == buscar_id:
		print("ID encontrado en la base de datos:" f" {buscar_id}")
		break
else:
	print("ID no encontrado en la base de datos")

# Esto  serviria para encontrar un ID en una base de datos por ejemplo en una busqueda
# de un usuario en una base de datos de usuarios

for char in "Fernando Leon Franco":
	print(char)