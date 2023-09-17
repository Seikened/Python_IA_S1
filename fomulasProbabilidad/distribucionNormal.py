from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la probabilidad acumulada para un x dado
def normal(x, mu, sigma):
    z = (x - mu) / sigma
    prob_acumulada = norm.cdf(z)
    print(f"La probabilidad acumulada P(x <= {x}) es {prob_acumulada}")

    # Graficar la distribución
    x_values = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    y_values = norm.pdf((x_values - mu) / sigma)

    plt.plot(x_values, y_values, label='Distribución Normal')
    plt.axvline(x, color='red', linestyle='--', label=f'x={x}')
    plt.fill_between(x_values, y_values, where=(x_values <= x), color='red', alpha=0.5, label=f'P(x <= {x})')
    plt.title('Distribución Normal')
    plt.xlabel('x')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()
    plt.show()

# Función para encontrar z para una probabilidad acumulada dada
def encontrar_z(prob_acumulada):
    z = norm.ppf(prob_acumulada)
    print(f"El valor de z tal que P(Z < z) = {prob_acumulada} es {z}")

# Preguntar al usuario qué operación quiere realizar
opcion = input("¿Qué deseas hacer?\n1. Calcular probabilidad acumulada para un x dado\n2. Encontrar z para una probabilidad acumulada dada\nElige 1 o 2: ")

if opcion == '1':
    x = float(input("Ingrese el valor de x: "))
    mu = float(input("Ingrese el valor de mu: "))
    sigma = float(input("Ingrese el valor de sigma: "))
    normal(x, mu, sigma)
elif opcion == '2':
    prob_acumulada = float(input("Ingrese la probabilidad acumulada: "))
    encontrar_z(prob_acumulada)
else:
    print("Opción no válida.")
