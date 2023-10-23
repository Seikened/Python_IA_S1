import math as mt
import matplotlib.pyplot as plt


ln_valores = []
x_valores = []

print("\n  x   |  Valor de Ln(1+x)")
print("-----------|--------------")


x = 0.00001
while x < 0.99:
    ln_actual = mt.log(1+x)
    print("%10.3f | %10.3f" % (x, ln_actual))
    
    x_valores.append(x)
    ln_valores.append(ln_actual)
    
    x += 0.01

# Crear un gráfico de los valores
plt.plot(x_valores, ln_valores, color="#11d1dd", linestyle="--", marker="o", label="Valor de Ln(1+x)") 
plt.title("Valores de Ln(1+x)") 
plt.ylabel("Ln(1+x)") 
plt.xlabel("x") 
plt.grid(True) 
plt.legend() 

plt.show()
