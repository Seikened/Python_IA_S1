numero = int(input("Ingrese el numero para calcular su sumatoria: "))
contador = numero
numeroSumado = 0

while contador > 0:
    numeroSumado += contador
    contador -= 1
    
print(f"Número sumado: {numeroSumado}")
