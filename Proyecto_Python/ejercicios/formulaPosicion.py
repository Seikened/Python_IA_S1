# Formula para calcular la posición de un objeto que cae


# posicionInicial_m = float(input("Ingrese la posición inicial: "))
# velocidadInicial_m_s = float(input("Ingrese la velocidad inicial: "))
# tiempo_s = float(input("Ingrese el tiempo: "))
# constante = 0.5
# aceleracion_m_s2 = float(input("Ingrese la aceleración: "))
# tiempoCuadrado_s2 = tiempo_s ** 2
#
# calculoPosicion = posicionInicial_m + (velocidadInicial_m_s * tiempo_s) + (constante * aceleracion_m_s2 * tiempoCuadrado_s2)
# print("La posición del objeto es: ", calculoPosicion)


posicionInicial_m = 10.0
velocidadInicial_m_s = 10.0
tiempo_s = 15.0
constante = 0.5
aceleracion_m_s2 = -9.81
tiempoCuadrado_s2 = tiempo_s ** 2.0

calculoPosicion = posicionInicial_m + (velocidadInicial_m_s * tiempo_s) + (constante * aceleracion_m_s2 * tiempoCuadrado_s2)
print("La posición del objeto es: ", calculoPosicion)