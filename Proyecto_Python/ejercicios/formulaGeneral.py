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
