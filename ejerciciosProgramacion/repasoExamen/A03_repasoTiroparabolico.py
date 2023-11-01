import matplotlib.pyplot as plt

alturaOriginal_m = 10
velocidadOriginal_m_s = 15
aceleracionGravedad_m_s2 = -9.81
tiempo_s = 0
alturaObjeto = 10

listaTiempo = []
listaObjeto = []
print("Tiempo    |  Altura del objeto")
print("----------|-------------------")

while  alturaObjeto > 0:
    alturaObjeto = alturaOriginal_m + ( velocidadOriginal_m_s * tiempo_s ) + ( .5 * ( aceleracionGravedad_m_s2 * ( tiempo_s ** 2 ) ) )
    print("  %6.2f  |   %6.2f" %(tiempo_s, alturaObjeto))
    listaTiempo.append(tiempo_s)
    listaObjeto.append(alturaObjeto)
    tiempo_s += .01
    





plt.plot(listaTiempo,listaObjeto, color="#11d1dd", linestyle="--", label="Altura Objeto") 
plt.title("Tiro parabolico")
plt.xlabel("Tiempo [s]")
plt.ylabel("Altura [m]")
plt.grid(True)
plt.legend()
plt.show()
