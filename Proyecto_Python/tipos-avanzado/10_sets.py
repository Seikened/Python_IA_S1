# Set significa conjunto, es una colección de elementos únicos y desordenados
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 4, 5]
segundo = set(segundo)
print(primer | segundo)  # Union
print(primer & segundo)  # Intersección
print(primer - segundo)  # Diferencia esto le quita los elementos que tiene en común pero solo al primer set
print(primer ^ segundo)  # Diferencia simétrica

if 5 in segundo:
	print("Si esta")
