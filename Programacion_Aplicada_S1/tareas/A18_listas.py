listaNumerosFlotantes = []
cantidadNumerosLista = int(input("¿De cuantos números quieres tu lista? "))
numeroMayor = float('-inf')
numeroMenor = float('inf')
sumaTotal = 0
promedio = 0

for _ in range(cantidadNumerosLista):
    numeroFlotante = float(input("Introduce tu número: "))
    listaNumerosFlotantes.append(numeroFlotante)
    
print(f"Tu lista es: {listaNumerosFlotantes}")


for numero in listaNumerosFlotantes:
    if numero > numeroMayor: numeroMayor = numero
    if numero < numeroMenor:numeroMenor = numero
    
print(f"""
El menor de tus números es: {numeroMenor}
El mayor de tus núemros es: {numeroMayor}
""")

for numero in listaNumerosFlotantes:
    sumaTotal += numero 
    
promedio = sumaTotal/ len(listaNumerosFlotantes)

print(f"El promedio de tu lista {listaNumerosFlotantes} es: {promedio}")
