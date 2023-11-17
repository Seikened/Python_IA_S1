import math as mt
import matplotlib.pyplot as plt

# Funcion 1
def maria():
    listaTiempo = []
    listaFuncion = []
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




# Funcion 2
def gael():
    sumatoria = 0
    x= int(input("Que valor quieres usar: "))
    
    for n in range(1,6,1):
        
        sumatoria += ( 2 * n ) / ( (x**n) +2 )
        print(sumatoria)






print("ESTOYT SOLO HABLANDO CON MARIN")
if __name__ == "__main__": # Este código es necesario para importar
    print("")
