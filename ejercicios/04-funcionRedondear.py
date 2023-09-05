numeroDecimal =  9.86567
int(input("Ingrese el numero de decimales que desea: "))
factor = 10 ** n_decimales


# Un números decimales
numeroUnDigitos = numeroDecimal
reduccionDecimalUnDigito = (numeroUnDigitos + 0.05)
reduccionDecimalUnDigito *=  10
reduccionDecimalUnDigito = int(reduccionDecimalUnDigito)
reduccionDecimalUnDigito /=  10

print("El numero decimal ingresado es: ", reduccionDecimalUnDigito)
# Dos números decimales
numeroDosDigitos = numeroDecimal
reduccionDecimalDosDigitos = (numeroDosDigitos + 0.005)
reduccionDecimalDosDigitos *=  100
reduccionDecimalDosDigitos = int(reduccionDecimalDosDigitos)
reduccionDecimalDosDigitos /=  100

print("El numero decimal ingresado es: ", reduccionDecimalDosDigitos)
# Tres números decimales
numeroTresDigitos = numeroDecimal
reduccionDecimalTresDigitos = (numeroTresDigitos + 0.0005)
reduccionDecimalTresDigitos *=  1000
reduccionDecimalTresDigitos = int(reduccionDecimalTresDigitos)
reduccionDecimalTresDigitos /=  1000

print("El numero decimal ingresado es: ", reduccionDecimalTresDigitos)