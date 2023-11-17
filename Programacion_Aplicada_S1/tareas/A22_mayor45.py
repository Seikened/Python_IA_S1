import math as mt
import matplotlib.pyplot as plt


pi = mt.pi
velocidadInicial_m_s = 400
aceleracion_m_s2 = -9.81

distanicaMisilVector = []
anguloVector = []

print("\n  Angulo   |  Distancia del cañon")
print("-----------|--------------")
contador = 45
while contador < 90:
    angulo = contador
    radianes = (pi * angulo) / 180
    distanicaMisil = ((-2 * (velocidadInicial_m_s**2) ) * (mt.cos(radianes) * mt.sin(radianes))) / aceleracion_m_s2
    print("%10.2f | %10.2f" % (angulo,distanicaMisil))
    distanicaMisilVector.append(distanicaMisil)
    anguloVector.append(angulo)
    contador += .001


print("\n")

# Verificar que exista el mayor y los disparos angulos son resultados similares
distanciaDeseada = 10000
distanciaConseguida = None
anguloConseguido = None 


for distancia, angulo in zip(distanicaMisilVector, anguloVector):
    if distancia < distanciaDeseada:
        break
    else:
        anguloConseguido = angulo
        distanciaConseguida = distancia

    
    
print(f"Se encontro la distancia deseada de {distanciaDeseada} en el angulo {anguloConseguido} con una distancia de {distanciaConseguida}")





plt.plot(anguloVector,distanicaMisilVector, color="#11d1dd", linestyle="--", marker="o", label=" Distancia del cañon") 
plt.title("Simulación del disparo de un cañon") 
plt.ylabel("Distancia [m]") 
plt.xlabel("Angulo [°]") 
plt.grid(True) 
plt.legend() 


plt.show()

