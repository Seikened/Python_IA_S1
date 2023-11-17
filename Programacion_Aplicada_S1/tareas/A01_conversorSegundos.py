segundosEntrada = int(input("Ingrese la cantidad de segundos: "))

horas = segundosEntrada // 3600
segundosRestantes = segundosEntrada % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print(f"El tiempo ingresado es: {horas} horas, {minutos} minutos y {segundos} segundos.")
