import pandas as pd

df = pd.read_csv('datosFinales.csv')

cantidadPaisesDiferentes = df['PAIS_NACIONALIDAD'].nunique()

print(f"Número de países diferentes: {cantidadPaisesDiferentes}")
