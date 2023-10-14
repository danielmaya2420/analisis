import pandas as pd

# Cargar el conjunto de datos limpio
df = pd.read_csv('datosFinales.csv')

# Filtrar las personas que cumplen con los criterios
personas_cumplen_criterios = df[(df['NEUMONIA'] == 1) & (df['EDAD'] >= 20) & (df['EDAD'] <= 40) & (df['EMBARAZO'] == 1)]

# Obtener la cantidad de personas que cumplen con los criterios
cantidad_personas_cumplen_criterios = len(personas_cumplen_criterios)

# Obtener la cantidad total de registros en la base de datos
cantidad_total_registros = len(df)

# Calcular el porcentaje
porcentaje = (cantidad_personas_cumplen_criterios / cantidad_total_registros) * 100

print(f'Cantidad de personas con NEUMONIA = 1, edad entre 20 y 40 años, y EMBARAZO = 1: {cantidad_personas_cumplen_criterios}')
print(f'Porcentaje respecto al total de registros: {porcentaje:.2f}%')
