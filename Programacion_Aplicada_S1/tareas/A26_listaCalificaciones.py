import random


def capturaAlumnos(numeroAlumnos):
    #numeroAlumnos = #int(input("¿Cuantos alumnos registraras? "))
    alumno = []
    miGrupo = []
    for numero in range(numeroAlumnos):
        #nombre = input(f"¿Como se llama el alumno {numero+1}? ").upper()
        #calificacion = float(input(f"¿Cuál es su calificación del alumno {numero+1}? "))
        #Gnerare alumnos y calificaciones al azar
        nombre = F"ESTUDIANTE {numero}"
        calificacion = random.randint(0,10)
        
        alumno = [nombre,calificacion]
        miGrupo.append(alumno)
    return miGrupo

def promedioGrupo(listaAlumnos):
    sumaGrupo =0
    for alumno in listaAlumnos:
        sumaGrupo += alumno[1]
    return sumaGrupo / len(listaAlumnos)


def MaximaCalificacion(listaAlumnos):
    calificacionMayor = -1000000
    for alumno in listaAlumnos:
        if alumno[1] > calificacionMayor:
            calificacionMayor = alumno[1]
    return calificacionMayor


#ordenamiento burbuja
def OrdenaBurbuja(listaAlumnos):
    for _ in range (0, len (listaAlumnos) -1) :
        for numeroAlumno in range (0, len (listaAlumnos) -1) :
            # #intercambia los valores entre lista[j] y listalj+1]
            if (listaAlumnos[numeroAlumno+1] [1])< (listaAlumnos[numeroAlumno] [1]):
                (listaAlumnos[numeroAlumno] ,listaAlumnos[numeroAlumno+1] )=(listaAlumnos[numeroAlumno+1] ,listaAlumnos[numeroAlumno])




# Programa principal
alumnos = capturaAlumnos(30)
print("Lista de alumnos:", alumnos)
print("Promedio del grupo:", promedioGrupo(alumnos))
print("Calificación máxima:", MaximaCalificacion(alumnos))
OrdenaBurbuja(alumnos)
print("Lista de alumnos ordenada:", alumnos)