import matplotlib.pyplot as plt

alturaOriginal_m = 5
velocidadOriginal_m_s = 10
aceleracion_s_s2 = -9.81
tiempo = 0
alturaObjeto_m = 5
time = []
height = []


while (alturaObjeto_m >= 0):
    alturaObjeto_m = alturaOriginal_m + (velocidadOriginal_m_s * tiempo) + ((.5 * aceleracion_s_s2) * (tiempo ** 2))
    time.append(tiempo)
    height.append(alturaObjeto_m)

    tiempo += 0.1
print("Toco el piso")


# Visualización
#plt.figure(figsize=(10, 6)) esto es para cambiar el tamaño de la imagen de ser necesario
# En la gráfica de abajo se puede cambiar el color de la línea, el estilo de la línea, el marcador y el nombre de la leyenda
plt.plot(time, height, color="#11d1dd", linestyle="--", marker="o", label="Altura del objeto")
plt.title("Simulación de un Objeto en Caída Libre") # Esto es para ponerle un título a la gráfica
plt.xlabel("Tiempo [s]") # Esto es para ponerle un nombre al eje x
plt.ylabel("Altura [m]") # Esto es para ponerle un nombre al eje y
plt.grid(True) # Esto es para ponerle una cuadrícula a la gráfica
plt.legend() # Esto es para abrir la leyenda de las etiquetas que se pusieron en la gráfica

# plt.savefig("simulacion_caida_libre.svg") esto es para guardar la imagen
plt.show()


# import math

# x = []
# y = []

# a = 0 
# radio = 0
# while a<6.3:
#     esteX = radio*math.cos(a)
#     esteY = radio*math.sin(a)
#     x.append(esteX)
#     y.append(esteY)
#     radio += 1
#     a += .001

# # Se muestra la gráfica con los datos bonitos
# plt.plot(x,y, color="#11d1dd", linestyle="-", label="Altura del objeto")
# plt.show()