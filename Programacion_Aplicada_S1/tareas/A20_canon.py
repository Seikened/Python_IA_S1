import math as mt
import matplotlib.pyplot as plt


pi = mt.pi
velocidadInicial_m_s = 400
aceleracion_m_s2 = -9.81

distanicaMisilVector = [0 for _ in range(19)]
anguloVector = [0 for _ in range(19)]

print("\n  Angulo   |  Distancia del cañon")
print("-----------|--------------")

gradoDerecho = 0
listaGradoDerecho = []
for i,angulo in enumerate(range(0,91,5)):
    radianes = (pi * angulo) / 180
    distanicaMisil = ((-2 * (velocidadInicial_m_s**2) ) * (mt.cos(radianes) * mt.sin(radianes))) / aceleracion_m_s2
    print("%10.2f | %10.2f" % (angulo,distanicaMisil))
    distanicaMisilVector[i] = distanicaMisil # type: ignore
    anguloVector[i] = angulo    

print("\n")


# Verificar que exista el mayor y los disparos angulos son resultados similares
distanciaMayor = 0
anguloMayor = 0 

# Verificación de angulos iguales dentro del vector dando que dos angulos pueden dar la misma distancia
numeroDeVecesDistancia = []
nuevaEntrada = {}
for i, (distancia, angulo) in enumerate(zip(distanicaMisilVector, anguloVector)):
    
    if distanciaMayor < distancia:
        distanciaMayor = distancia
        anguloMayor = angulo

    # Creamos la nueva entrada dentro del bucle para que tome los valores actuales
    nuevaEntrada = {
        "posicion": i,
        "angulo": angulo,
        "distancia": distancia  # Usamos la variable del bucle
    }
    
    # Verificar si la distancia ya existe en el diccionario
    distancias_existentes = [x["distancia"] for x in numeroDeVecesDistancia]
    if distancia in distancias_existentes:
        print(f"La distancia {distancia} ya existe para otro ángulo.")
    else:
        # Si no existe, añadimos la nueva entrada al diccionario
        numeroDeVecesDistancia.append(nuevaEntrada)

print(numeroDeVecesDistancia)
print(f"El mejor angulo del cañon desde: {anguloVector[0]} hasta: {anguloVector[-1]} es el angulo {anguloMayor}")


plt.plot(anguloVector,distanicaMisilVector, color="#11d1dd", linestyle="--", marker="o", label=" Distancia del cañon") 
plt.title("Simulación del disparo de un cañon") 
plt.ylabel("Distancia [m]") 
plt.xlabel("Angulo [°]") 
plt.grid(True) 
plt.legend() 


plt.show()