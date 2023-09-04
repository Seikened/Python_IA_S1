# def billetes(monto, valor_billete):
#     cantidad_billetes = monto // valor_billete
#     monto %= valor_billete
#     return monto, cantidad_billetes
#
# monto = int(input("Ingrese el monto: "))
# monto_copia = monto
#
# monto, billete_1000 = billetes(monto, 1000)
# monto, billete_500 = billetes(monto, 500)
# monto, billete_200 = billetes(monto, 200)
# monto, billete_100 = billetes(monto, 100)
# monto, billete_50 = billetes(monto, 50)
#
# if monto == 0:
#     print("Se puede dar el monto exacto")
#     print("Billetes de 1000:", billete_1000)
#     print("Billetes de 500:", billete_500)
#     print("Billetes de 200:", billete_200)
#     print("Billetes de 100:", billete_100)
#     print("Billetes de 50:", billete_50)
#     print("Monto:", monto_copia)
# else:
#     print("No se puede dar el monto exacto")




# Programa de cajero automático para entregar la menor cantidad de billetes


RetiroTotal = int(input("Introduce tu cantidad multiplos de 50: ")) # Total a retirar

# Billetes de 500
B500 = RetiroTotal // 500 # Esto es para sumar y mostrar la cantidad de billetes de 500 al usuario
RetiroTotal %= 500 # Esto da el resto de la división de RetiroTotal entre 500 (el monto que falta por entregar) para calculo interno
print("Billetes de 500: ", B500)

# Billetes de 200
B200 = RetiroTotal // 200
RetiroTotal %= 200
print("Billetes de 200: ", B200)

# Billetes de 100
B100 = RetiroTotal // 100
RetiroTotal %= 100
print("Billetes de 100: ", B100)

# Billetes de 50
B50 = RetiroTotal // 50
RetiroTotal %= 50
print("Billetes de 50: ", B50)
