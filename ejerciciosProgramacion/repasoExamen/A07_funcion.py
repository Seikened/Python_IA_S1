import math as mt
listaTiempo = []
listaFuncion = []
import matplotlib.pyplot as plt

pi = mt.pi


tiempoUsuario = int(input("Cuanto tiempo quieres que dure [s]: "))

for tiempo in range(tiempoUsuario):
    funcionTiempo = mt.cos( tiempo / (0.2 * pi ) ) * mt.exp( -tiempo / 10)
    listaTiempo.append(tiempo)
    listaFuncion.append(funcionTiempo)

plt.plot(listaTiempo,listaFuncion, color="#11d1dd", linestyle="-", label="Trazado o comportamiento")
plt.xlabel("Tiempo [s]")
plt.ylabel("Función de tiempo")
plt.title("Sistema amortiguado")
plt.legend()
plt.show()