numero = int(input("Ingrese el numero para calcular su factorial: ")) #5
contador = numero # 5
numeroFactorial = 1 # 5

while contador > 0:
    numeroFactorial = numeroFactorial * contador
    contador = contador - 1
    
print(f"Número factorial: {numeroFactorial}")
