import math  # Para la constante de Euler

def factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def distribucionPoisson(lambda_var, numero_ocurrencias):
    euler = math.e  # Usamos la constante de Euler del módulo math
    resultado = ((lambda_var ** numero_ocurrencias) * (math.exp(-lambda_var))) / factorial(numero_ocurrencias)
    return resultado

if __name__ == '__main__':
    lambda_var = float(input("Ingrese el valor de lambda: "))
    numero_ocurrencias = int(input("Ingrese el valor de número de ocurrencias: "))
    print(f"La distribución de Poisson es: {distribucionPoisson(lambda_var, numero_ocurrencias)}")
