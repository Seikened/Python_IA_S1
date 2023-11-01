#lista de calificaciones


grupos= []
for i in range (0,3) :
    nombre=input ("Nombre?")
    parcial_1=float (input ("Primer parcial: "))
    parcial_2=float (input ("Segundo parcial: ") )
    parcial_3=float (input ("Tercer parcial: "))
    parciales=[parcial_1, parcial_2,parcial_3]
    alumno= [nombre, parciales]
    grupos.append (alumno)
    
#Aqui mostrarlos
print(grupos)

