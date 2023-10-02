import random
import pandas as pd

lanzamientos = []
for i in range(1, 1000, 1):
	lanzamientos.append(random)
datos = pd.DataFrame()
datos['Lanzamientos_dado'] = lanzamientos

datos['Lanzamientos_dado'].hist()
