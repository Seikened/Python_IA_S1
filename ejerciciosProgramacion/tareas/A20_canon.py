import math as mt
import matplotlib.pyplot as plt


pi = mt.pi
velocidadInicial_m_s = 400
aceleracion_m_s2 = -9.81

distanicaMisilVector = [0 for _ in range(19)]
anguloVector = [0 for _ in range(19)]

print("\n  Angulo   |  Distancia del cañon")
print("-----------|--------------")

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
angulosIguales = []
distanciasIguales = []
numero_de_vecesDistancia = [

for distancia,angulo in zip(distanicaMisilVector,anguloVector): # La función zip() me permite iterar 2 vectores al mismo tiempo ya que tienen el mismo tamaño me conviene
    if distanciaMayor < distancia:
        distanciaMayor = distancia
        anguloMayor = angulo
    # Verificación de angulos iguales
    if angulo in anguloVector:
        

print(f"El mejor angulo del cañon desde: {anguloVector[0]} hasta: {anguloVector[-1]} es el angulo {anguloMayor}")

# Verificamos cuales angulos obtienen el mismo resultado



plt.plot(anguloVector,distanicaMisilVector, color="#11d1dd", linestyle="--", marker="o", label=" Distancia del cañon") 
plt.title("Simulación del disparo de un cañon") 
plt.ylabel("Distancia [m]") 
plt.xlabel("Angulo [°]") 
plt.grid(True) 
plt.legend() 


plt.show()

