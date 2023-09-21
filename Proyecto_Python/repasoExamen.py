miVariableUnicaEntera = 10
miVariableUnicaFlotante = 1.123
miVariableUnicaBoleana = True
miVariableUnicaString = "Mi mensaje para el mundo tipo cadena de texto"

# Primer ejercicio
# Conversor de segundos

userSegundo = int(input("Introduce los segundos para convertirlos a horas,min y segundos"))

horas = userSegundo//3600
tiempoRestante = userSegundo % 3600
minutos = tiempoRestante // 60
segundos = tiempoRestante % 60

print(f"Tiempo convertido en horas: {horas} con minutos: {minutos} y {segundos} segundos")

# Formula general

a = 30
b = 10
c = 20


formulaGeneralPositiva = (-b+(.5**(b**2-4*a*c)))/(2*a)
formulaGeneralNegativa = (-b-(.5**(b**2-4*a*c)))/(2*a)

print(f"La formula general positiva da: {formulaGeneralPositiva} y la formula general negativa da: {formulaGeneralNegativa}")

# Número mayor de 3 numeros dados

primerValor = float(input("Introdusca el primer valor"))
segundoValor =  float(input("Introdusca el segundo valor"))
tercerValor =  float(input("Introdusca el tercer valor"))
valorMayor = primerValor

if segundoValor > valorMayor:
	valorMayor = segundoValor

if tercerValor > valorMayor:
	valorMayor = tercerValor

print(f"El mayor de los 3 números, primer valor{primerValor}, segundo valor {segundoValor} y tercer valor {tercerValor} es: {valorMayor}")

# Operaciones básicas
primerValorOperacion = float(input("Introduce tu primer valor"))
segundoValorOperacion = float(input("Introduce tu segundo valor"))

suma = primerValorOperacion + segundoValorOperacion
resta = primerValorOperacion - segundoValorOperacion
multi = primerValorOperacion * segundoValorOperacion
division = primerValorOperacion / segundoValorOperacion
potencia = primerValorOperacion ** segundoValorOperacion
divisionEntera = primerValorOperacion // segundoValorOperacion
print(f"""
Suma:{suma}
Resta:{resta}
Multiplicación:{multi}
División:{division}
Potencia:{potencia}
División entera:{divisionEntera}
""")

# Tornillos en 1D

posicionTornillo1D = int(input("Introduce la posición del tornillo 1D: "))

distanciaTornilloX_mm = (posicionTornillo1D * 15) + 7.5

print(f"Tu tornillo en la posición: {posicionTornillo1D} tiene una distancia de: {distanciaTornilloX_mm}")

# Tornillo 2d
posicionTornillo2D = int(input("Introduce la posición del tornillo 2D: "))
renglon = posicionTornillo2D // 8
columna = posicionTornillo2D % 8

distanciaTornilloX_mm = (columna * 15) + 7.5
distanciaTornilloY_mm = (renglon * 15) + 7.5

print(f"Tus coordenadas en x,y de tu tornillo en la posición: {posicionTornillo2D} son x: {distanciaTornilloX_mm} y en Y: {distanciaTornilloY_mm}")

# Tornillo 2d pero pidiendo las cordenadas
cX = float(input("Introduce la coordenada en el eje x: "))
cY = float(input("Introduce la coordenada en el eje Y: "))

renglon = cY//15
columna = cX//15
posicionTornillo = renglon * 8 + columna

print(f"Tu posición de tus coordenadas x: {cX} y Y: {cY} es el tornillo: {posicionTornillo}")