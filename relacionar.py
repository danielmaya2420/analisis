import pandas as pd

# Cargar los datos principales desde datosFinales.csv
df_principal = pd.read_csv('datosFinales.csv')

# Definir una función para buscar y asignar descripciones desde el catálogo
def mapear_descripcion(columna, hoja_catalogo):
    catalogo = pd.read_excel('catalogo.xlsx', sheet_name=hoja_catalogo)
    mapeo = dict(zip(catalogo['CLAVE'], catalogo['DESCRIPCIÓN']))
    return columna.map(mapeo)

# Leer el archivo relacionar.xlsx para obtener las columnas y sus respectivas hojas de catálogo
df_relacionar = pd.read_excel('relacionar.xlsx')

# Iterar a través de las filas de df_relacionar para mapear las columnas
for _, fila in df_relacionar.iterrows():
    if 'BUSCAR EN' in fila.index:
        nombre_columna = fila['NOMBRE DE VARIABLE']
        hoja_catalogo = fila['BUSCAR EN']
        if nombre_columna in df_principal.columns:
            df_principal[nombre_columna + '_DESCRIPCION'] = mapear_descripcion(df_principal[nombre_columna], hoja_catalogo)

# Guardar el DataFrame con las descripciones mapeadas en un nuevo archivo
df_principal.to_csv('datosFinales_con_descripciones.csv', index=False)
