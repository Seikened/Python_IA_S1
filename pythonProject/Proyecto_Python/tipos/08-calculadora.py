n1 = input("🏃🏼Ingresa el primer número: ")
n2 = input("😝Ingresa el segundo número: ")

n1 = int(n1)  # Convertir a entero
n2 = int(n2)  # Convertir a entero
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
division = n1 / n2
modulo = n1 % n2
potencia = n1 ** n2

mensaje = f"""
Para los números: {n1} y {n2}
🔹Para la suma es: {suma}
🔹Para la resta es: {resta}
🔹Para la multiplicación es: {multi}
🔹Para la división es: {division}
🔹Para el módulo es: {modulo}
🔹Para la potencia es: {potencia}
PARA
"""

print(mensaje)
