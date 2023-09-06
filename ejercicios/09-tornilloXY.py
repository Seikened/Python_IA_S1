def calcular_coordenadas_tornillo_corregido(numero_tornillo):
    distancia_x = 15  # Distancia entre tornillos en la misma columna es 15mm
    distancia_y = 15  # Corrección: Distancia entre renglones también es 15 mm

    # Calcular el renglón y la columna del tornillo
    renglon = numero_tornillo // 8  # División entera para encontrar el renglón ejemplo si es 13, 13//8 = 1
    columna = numero_tornillo % 8  # Resto de la división para encontrar la columna ejemplo si es 13, 13%8 = 5


    posicion_x = 7.5 + columna * distancia_x # Calcular las coordenadas x del tornillo
    posicion_y = 7.5 + renglon * distancia_y # Calcular las coordenadas y del tornillo

    return posicion_x, posicion_y

entradaUser = int(input("Ingrese la posicion del tornillo: "))
x,y=calcular_coordenadas_tornillo_corregido(entradaUser)
print(f"Para el tornillo 🔹{entradaUser}🔹 las coordenadas de X es: {x} | Y es: {y}")
