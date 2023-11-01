#lista de calificaciones


grupos= []
for i in range (0,3) :
    nombre=input ("Nombre?")
    parcial_1=float (input ("Parciall?"))
    parcial_2=float (input ("Parcia12?") )
    parcial_3=float (input ("Parcia13?"))
    parciales=[parcial_1, parcial_2,parcial_3]
    alumno1= [nombre, parciales]
    grupos.append (alumno1)
    
#Aqui mostrarlos
print(grupos)
