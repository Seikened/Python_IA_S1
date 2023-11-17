numeros = [10, 5, 6, 8, 9, 1, 2, 3, 4, 7]
# numeros.sort(reverse=True)

numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [['Eduardo', 35], ['Fernando', 18], ['Maria', 25], ['Andres', 21]]

usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)  # Solo ordena por el primer elemento de la lista
