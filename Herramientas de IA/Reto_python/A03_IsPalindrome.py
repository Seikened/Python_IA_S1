palabraVerificar =  str(input("Introduce tu palabra: ")).lower()
palabraCopiar = list(palabraVerificar)
palabraVolteada = []

for letra in palabraVerificar[-1]:
    palabraVolteada.append(letra)

if palabraCopiar == palabraVolteada:
    print("Es palibdroma")
else:
    print("No es palindroma")


