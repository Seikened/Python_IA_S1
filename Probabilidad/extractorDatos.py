from operator import index
import numpy as np
import pandas as pd
import locale
import matplotlib.pyplot as plt
from scipy.stats import norm

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

ruta = "/Users/fernandoleon/PycharmProjects/Python_IA_S1/Probabilidad/dataBase.csv"

# Leer los datos del archivo csv
df = pd.read_csv(ruta)
copiaDatos = df.copy()
columnasTotales = df.columns.tolist()
columnasMantener = ["Estado","Total","Tipo","Serie Folio","Created At"]
columnasBorrar = []

# Borrar las columnas que no se necesitan
for columna in columnasTotales:
    if columna not in columnasMantener: 
        columnasBorrar.append(columna)

# Borrar las columnas que no se necesitan
copiaDatos.drop(columnasBorrar, axis=1, inplace=True)

# Eliminar las filas que no se necesitan
indices_a_eliminar = copiaDatos[(copiaDatos['Tipo'] == 'cotizacion')].index
copiaDatos.drop(indices_a_eliminar, inplace=True)

indices_a_eliminar = copiaDatos[((copiaDatos['Estado'] == 'pendiente_pago') | (copiaDatos['Estado'] == 'cancelada'))].index
copiaDatos.drop(indices_a_eliminar, inplace=True)

# Guardar el DataFrame modificado como un nuevo archivo CSV
copiaDatos.to_csv("/Users/fernandoleon/PycharmProjects/Python_IA_S1/Probabilidad/dataBase_modificada.csv", index=False)

# Formatear la columna 'Created At' como fecha
copiaDatos['Created At'] = pd.to_datetime(copiaDatos['Created At'])

# Establecer la columna 'Created At' como el índice
copiaDatos.set_index('Created At', inplace=True)

# Agrupar por mes y calcular la suma de la columna 'Total'
sumaMes = copiaDatos.resample('M').sum()['Total']

# Promedio de la población por mes
promedioMensualPoblacion = sumaMes.mean()

# Estadísticas descriptivas
estadisticas = copiaDatos['Total'].describe()

promedioTotal = round(estadisticas['mean'], 2)

# Imprimir las estadísticas en el formato deseado
print(f"\n🔢 Número de entradas: {estadisticas['count']}")
print(f"💰 Promedio de ventas totales: {promedioTotal}")
print(f"📊 Desviación estándar: {round(estadisticas['std'], 2)}")
print(f"🔻 Venta mínima: {estadisticas['min']}")
print(f"📏 Primer cuartil: {estadisticas['25%']}")
print(f"🎯 Mediana: {estadisticas['50%']}")
print(f"📈 Tercer cuartil: {estadisticas['75%']}")
print(f"🔺 Venta máxima: {estadisticas['max']}\n")

# Promedio de sumas mensuales
print(f"🧮 Promedio de sumas mensuales: {locale.currency(round(promedioMensualPoblacion, 2), grouping=True)} \n")

# Se van a seleccionar 5000 datos de la población al azar
cantidadMuestras = 100
tamanoMuestras = 500
muestras =[]
mediasMuestras = []
for _ in range(cantidadMuestras):
    muestraActual = copiaDatos.sample(tamanoMuestras)
    muestras.append(muestraActual)
    mediaActual = muestraActual['Total'].mean()
    mediasMuestras.append(mediaActual)

plt.figure(figsize=(16, 8))
plt.hist(copiaDatos['Total'], bins=50, edgecolor='black', alpha=0.5)
plt.title('Histograma de Ventas de la población')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')

# Graficar la muestra
plt.figure(figsize=(16, 8))
plt.hist(mediasMuestras, bins=50, edgecolor='black', alpha=0.5)
plt.title('Histograma de Ventas de las Muestras')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')

# PASO 1 | Caso de estudio y plantear una hipótesis

"""
Caso de estudio: Se quiere determinar si la media de ventas de un mes seleccionado es mayor que el promedio mensual de ventas de todos los registros.

Hipótesis nula (H0): 
P= M <= promedio de ventas Totales
La media de ventas del mes seleccionado es igual al promedio mensual de ventas de todos los registros.

Hipótesis alternativa (H1): 
P = M > promedio de ventas Totales
La media de ventas del mes seleccionado es mayor que el promedio mensual de ventas de todos los registros.

Los datos de la muestra serán las ventas totales de un mes en específico.
"""

# PASO 2 | Establecer la prueba a utilizar

"""
Se utilizará la prueba de z para una muestra de cola derecha.
"""

# PASO 3 | Calcular la significancia y la confianza
significancia = 0.05 # significancia
confianza = 1 - significancia # confianza

# Datos de la muestra
promedioMuestral = sum(mediasMuestras)/len(mediasMuestras) # Promedio de la muestra
valorEstimado =  promedioTotal # Valor estimado de la población
# Sigma gorro o desviación estándar de la muestra
sigmaGorro  = np.std(mediasMuestras) # Desviación estándar de la muestra
tamanoMuestra = len(mediasMuestras) # Tamaño de la muestra
errorEstandar = sigmaGorro / tamanoMuestra**0.5 # Error estándar

z =  (promedioMuestral - valorEstimado) / errorEstandar # Estadístico de prueba (z)

print(f"""
📊 Estadísticas de la muestra:
Promedio muestral: {promedioMuestral}
Valor estimado: {valorEstimado}
Sigma gorro: {sigmaGorro}
Tamaño de la muestra: {tamanoMuestra}
Error estándar: {errorEstandar}
Z: {z}""")

# PASO 4 | Calcular el valor crítico y el p-value
"""
El valor crítico se calculará utilizando la tabla de distribución normal estándar.
El p-value se calculará utilizando la función de distribución acumulada de la distribución normal estándar.
"""

"""
Fer, esto edítalo como veas necesario para que sea uniforme al resto del código, que veo que tenemos estilos un poco distintos para programar
btw pasé el plt.show al final del código porque el código se detiene en la línea donde esté el plt.show() hasta que se cierre la ventana
"""
prueba1 = None
prueba2 = None

valorCritico = norm.ppf(confianza) #  este es el equivalente a =INV.NORM.ESTAND de excel
print("\nel valor crítico es: %5.4f" %(valorCritico))
if valorCritico > z:
    print("como Z (%5.4f) es menor que el valor critico (%5.4f), y estamos usando una prueba de cola derecha, H0 no se rechaza" %(z, valorCritico))
    prueba1 = True #  tomando en cuenta el valor critico, H0 no se rechaza
if valorCritico < z:
    print("como Z (%5.4f) es mayor que el valor critico (%5.4f), y estamos usando una prueba de cola derecha, H0 se rechaza" %(z, valorCritico))
    prueba1 = False #  si es falso, entonces no existe la evidencia suficiente para aceptar H0

pValueMayorQue = norm.cdf(z) #  este es el equivalente a =DISTR.NORM.ESTAND.N de excel
pValueMenorQue = 1 - pValueMayorQue #  y al igual que excel, te regresa el mayor que, por lo que hay que hacer 1-P para tener menor que
print("\nel pValue es: %5.4f" %(pValueMenorQue))
if pValueMenorQue > significancia:
    print("como la significancia (%3.2f) es menor que el p-Value (%5.4f), y estamos usando una prueba de cola derecha, H0 no se rechaza" %(significancia, pValueMenorQue))
    prueba2 = True #  tomando en cuenta pValue, H0 no se rechaza
if pValueMenorQue < significancia:
    print("como la significancia (%3.2f) es mayor que el p-Value (%5.4f), y estamos usando una prueba de cola derecha, H0 se rechaza" %(significancia, pValueMenorQue))
    prueba2 = False #  si es falso, entonces no existe la evidencia suficiente para aceptar H0

margen_error = valorCritico * errorEstandar
intervalo_confianza = (promedioMuestral, promedioMuestral + margen_error)


print(f"📈 Intervalo de confianza del {confianza * 100}% para la media de ventas mensuales: {intervalo_confianza}")


# PASO 5 | Tomar la decisión y concluir

if prueba1 is True and prueba2 is True: #  si no se rechaza con valor critico ni con pValue, podemos aceptar H0
    print("\nExiste evidencia estadistica para aceptar H0")
    print(r"Existe un 95% de confianza que la media de ventas del mes seleccionado sea menor o igual al promedio mensual de ventas de todos los registros.")
else: 
    print("\nExiste evidencia estadistica para rechazar H0")
    print(r"Existe un 95% de confianza que la media de ventas del mes seleccionado es mayor al promedio mensual de ventas de todos los registros.")
    
plt.show()
