import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Función de distribución normal
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



x = float(input("Ingrese el valor de x: "))
mu = float(input("Ingrese el valor de mu: "))
sigma = float(input("Ingrese el valor de sigma: "))

normal(x, mu, sigma)
