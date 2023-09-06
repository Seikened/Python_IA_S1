# Corrigiendo el código y volviendo a probar
def calcular_coordenadas_tornillo_corregido(numero_tornillo):
    distancia_x = 15  # Distancia entre tornillos en la misma columna
    distancia_y = 15  # Corrección: Distancia entre renglones también es 15 mm

    # Calcular el renglón y la columna del tornillo
    renglon = numero_tornillo // 8  # División entera para encontrar el renglón
    columna = numero_tornillo % 8  # Resto de la división para encontrar la columna

    # Calcular las coordenadas x, y del tornillo
    posicion_x = 7.5 + columna * distancia_x
    posicion_y = 7.5 + renglon * distancia_y

    return posicion_x, posicion_y

# Probando nuevamente con el número de tornillo 13
print(calcular_coordenadas_tornillo_corregido(0))
