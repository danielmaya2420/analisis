import pandas as pd

# Cargar el conjunto de datos limpio
df = pd.read_csv('datosFinales.csv')

# Filtrar las personas que fallecieron (FECHA_DEF distinta de '9999-99-99')
fallecidos = df[df['FECHA_DEF'] != '9999-99-99']

# Agrupar las edades y contar la cantidad de muertes en cada grupo
edades_con_muertes = fallecidos.groupby('EDAD')['FECHA_DEF'].count().reset_index()

# Encontrar la edad con más muertes
edad_max_muertes = edades_con_muertes[edades_con_muertes['FECHA_DEF'] == edades_con_muertes['FECHA_DEF'].max()]

# Imprimir los resultados
print(f'Edad con más muertes: {edad_max_muertes.iloc[0]["EDAD"]} años, con {edad_max_muertes.iloc[0]["FECHA_DEF"]} muertes.')
