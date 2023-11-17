import random
import matplotlib.pyplot as plt




listaConteo = [0 for i in range(16)]



for i in range(15):
    numero = random.randint(1, 15)
    listaConteo[numero] += 1



print("Resultados: ")
for i in range(1, 15):
    print("El número %d salió %d veces" % (i, listaConteo[i]))


#Graficar
plt.bar(range(1, 16), listaConteo[1:16])
plt.title("Gráfico de barras")
plt.xlabel("Número")
plt.ylabel("Cantidad de veces")
plt.show()