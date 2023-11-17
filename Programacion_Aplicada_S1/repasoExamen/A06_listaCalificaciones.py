#lista de calificaciones
import random

grupos= []
for i in range (0,3) :
    nombre= f"hola {i}" #input ("Nombre: ")
    parcial_1= random.randint(1,10)
    parcial_2= random.randint(1,10)
    parcial_3= random.randint(1,10)
    parciales=[parcial_1, parcial_2,parcial_3]
    alumno= [nombre, parciales]
    grupos.append (alumno)
    
print("----------------------------------------------------------------")
print("Nombre               |   P1   |   P2   |   P3   |   Promedio   |")
print("----------------------------------------------------------------")
for index in grupos:
    nombre = index [0]
    parcial_Uno = index[1] [0]
    parcial_Dos = index [1] [1]
    parcial_Tres = index [1] [2]
    promedio = (parcial_Uno + parcial_Dos + parcial_Tres)/ len(index[1])
    print(f"{nombre:^20} | {parcial_Uno:^6} | {parcial_Dos:^6} | {parcial_Tres:^6} | {promedio:^12.2f} |")
    print("----------------------------------------------------------------")
#Aqui mostrarlos

print(grupos)
