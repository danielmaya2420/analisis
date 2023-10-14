import pandas as pd

df = pd.read_csv('datosFinales.csv')

cantidadRegistrosPais = df['PAIS_NACIONALIDAD'].value_counts()

cantidadRegistrosPais.to_csv('cantidadPorPais.csv', header=True)

