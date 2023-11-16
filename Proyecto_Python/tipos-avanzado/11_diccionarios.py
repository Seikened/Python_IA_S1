punto = {
	"x": 25,
	"y": 50,
}

print(punto["x"])
print(punto["y"])

punto["z"] = 20
print(punto)
if "lala" in punto:
	print("Encontre lala", punto["lala"])
else:
	print("No encontre lala")

print(punto.get("x"))
print(punto.get("w",97))

del punto["x"]
del(punto["y"])

print(punto)

punto["x"] = 50

for valor in punto:
    print(valor,punto[valor])


for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(valor, llave)


usuarios = [
	{"id":1, "nombre":"chanchito"},
	{"id":2, "nombre":"Fernando"},
	{"id":3, "nombre":"Leon"}
]

for usuario in usuarios:
    print(usuario["nombre"])

