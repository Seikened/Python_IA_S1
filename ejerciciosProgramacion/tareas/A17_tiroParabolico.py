# 3.- Considere un ejemplo de tiro parabólico donde
# y = yo + vo ⋅ t + 1 a ⋅ t 2 , 2
# donde y es la altura del objeto, yo es la altura original (5 metros), vo es la velocidad original (10 m/s), a es la aceleración de la gravedad (-9.81 m/s2), y t es el tiempo. El nivel del piso se alcanza cuando y es igual a cero.
# Escriba un programa que muestre en una tabla la altura y como función del tiempo t, desde el momento t = 0 s hasta que el objeto alcance una altura y = 0 m.
# La tabla se debería ver como lo que sigue:
# Notas:
# 1) Use un ciclo while para generar la tabla.
# 2) El incremento de tiempo debe ser de 0.1 s entre renglón y renglón.
# 3) La condición del ciclo para terminar es que el objeto haya alcanzado el piso (y <= 0).


alturaOriginal_m = 5
velocidadOriginal_m_s = 10
aceleracion_s_s2 = -9.81
tiempo = 0
alturaObjeto = 1

print(" Tiempo  |   Altura de Y")
print("---------|---------------")

while (alturaObjeto >= 0):
	alturaObjeto = alturaOriginal_m + (velocidadOriginal_m_s * tiempo) + ((.5 * aceleracion_s_s2) * (tiempo ** 2))
	print(" %6.2f  | %6.2f" % (tiempo, alturaObjeto))
	tiempo += 0.1
print("Toco el piso")
