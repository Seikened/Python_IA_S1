# Formula general
import math as mt

a = 20
b = 16
c = 3
raiz = (mt.sqrt((b ** 2) - 4 * (a * c)))

xPositiva = ((-b) + raiz)  / (2 * a)
xNegativa = ((-b) - raiz) / (2 * a)

print(f"""
x en positivo es: {xPositiva}
x en negativo es: {xNegativa} 
""")
# Revisar si la formula general esta bien
xMas=xNegativa
xMenos=xPositiva
ecuacionMas = a * (xMas ** 2) + b * xMas + c
ecuacionMenos = a * (xMenos ** 2) + b * xMenos + c
