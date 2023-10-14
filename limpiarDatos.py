import pandas as pd

df = pd.read_csv('datosFinales.csv')

#columnas_a_eliminar = ['ID_REGISTRO', 'ORIGEN', 'ENTIDAD_UM', 'ENTIDAD_NAC', 'ENTIDAD_RES', 'FECHA_ACTUALIZACION']

columnas_a_eliminar = ['HABLA_LENGUA_INDIG']
df = df.drop(columns=columnas_a_eliminar)

#df = df[df['FECHA_DEF'] != '9999-99-99']

df.to_csv('datoslimpios.csv', index=False)

