import pandas as pd

df = pd.read_csv('analizar.csv')

cantidad_total_registros = df.shape[0]

print(f"Cantidad total de registros: {cantidad_total_registros}")