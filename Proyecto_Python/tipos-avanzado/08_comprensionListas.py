usuarios = [
	["Chanchito feliz", 25],
	["Felipe", 1],
	["Pulga", 14],
]

# nombres = []
#
# for usuario in usuarios:
# 	nombres.append(usuario[0])
#
# print(nombres)
# Map
# nombre = [usuario[0] for usuario in usuarios]
# Filtrar - filter
# nombre = [ usuario for usuario in usuarios if usuario[1]  > 2 ]
# Filtrar y transformar
# nombre = [ usuario[0] for usuario in usuarios if usuario[1]  > 2 ]

# nombres =list(map(lambda usuario: usuario[0],usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(menosUsuarios)
