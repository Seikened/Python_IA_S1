punto = {
	"x":25,
	"y":50
}

print(punto["x"])
print(punto["y"])

punto["z"] = 20
print(punto)
if "lala" in punto:
	print("Encontre lala",punto["lala"])
else:
	print("No encontre lala")