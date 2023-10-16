import pandas as pd
import locale


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

ruta= "/Users/fernandoleon/PycharmProjects/Python_IA_S1/Probabilidad/dataBase.csv"

# Aqui se leen los datos del archivo csv
df = pd.read_csv(ruta) #Leer el archivo csv
copiaDatos = df.copy() #Copiar el archivo csv en otro dataframe
columnasTotales = df.columns.tolist()
columnasMantener = ["Estado","Total","Tipo","Serie Folio","Created At"]
columnasBorrar = []

# Vamos a borrar las columnas que no se necesitan
for columna in columnasTotales:
    if columna not in columnasMantener: 
        columnasBorrar.append(columna)
    

    
# TRATAMIENTO DE LA INFORMACIÓN
# Borrar las columnas que no se necesitan
copiaDatos.drop(columnasBorrar, axis=1, inplace=True) 
print("-------------------------------------------------- \n")
print(f"\n 🗑️ Cantidad de columnas borradas: {len(columnasBorrar)}")

# Eliminar las filas que no se necesitan
indices_a_eliminar = copiaDatos[(copiaDatos['Tipo'] == 'cotizacion')].index
copiaDatos.drop(indices_a_eliminar, inplace=True)

indices_a_eliminar = copiaDatos[((copiaDatos['Estado'] == 'pendiente_pago') | (copiaDatos['Estado'] == 'cancelada'))].index
copiaDatos.drop(indices_a_eliminar, inplace=True)



# Guardar el DataFrame modificado como un nuevo archivo CSV
copiaDatos.to_csv('/Users/fernandoleon/PycharmProjects/Python_IA_S1/Probabilidad/dataBase_modificado.csv', index=False)

# Formatear la columna 'Created At' como fecha (dato sacado de la documentación de pandas)
copiaDatos['Created At'] = pd.to_datetime(copiaDatos['Created At'])

# Establecer la columna 'Created At' como el índice (dato sacado de la documentación de pandas)
copiaDatos.set_index('Created At', inplace=True)

# Agrupar por mes y calcular la suma de la columna 'Total' (dato sacado de la documentación de pandas)
sumaMes = copiaDatos.resample('M').sum()['Total']


# Calcular el promedio de las sumas mensuales
promedioMensual = sumaMes.mean()

print(f"🧮 Promedio de sumas mensuales: {locale.currency(round(promedioMensual, 2), grouping=True)} \n")
print("\n-------------------------------------------------- \n")


# PASO 1 | Caso de estudio y plantear una hipótesis

# Hipótesis nula (H0): La media de ventas del mes seleccionado es menor o igual que el promedio mensual de ventas de todos los registros.
# Hipótesis alternativa (H1): La media de ventas del mes seleccionado es mayor que el promedio mensual de ventas de todos los registros.

# Nuestros datos seran tratados con las ventas totales del data set como la poblaicón
# Los datos de la muestra seran las ventas totales de un mes en específico