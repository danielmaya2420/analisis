import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos limpios
df = pd.read_csv('datosFinales.csv')

# Calcular los KPIs
kpi_resultados = {}

# Tasa de intubación
tasa_intubacion = (df['INTUBADO'] == 1).mean()
kpi_resultados['Tasa de intubación'] = tasa_intubacion * 100  # Convertir a porcentaje

# Tasa de neumonía
tasa_neumonia = (df['NEUMONIA'] == 1).mean()
kpi_resultados['Tasa de neumonía'] = tasa_neumonia * 100

# Promedio de edad
promedio_edad = df['EDAD'].mean()
kpi_resultados['Promedio de edad'] = promedio_edad



# Tasa de embarazo (para mujeres)
tasa_embarazo = (df['EMBARAZO'] == 1).mean()
kpi_resultados['Tasa de embarazo'] = tasa_embarazo * 100

# Tasa de población indígena
tasa_indigena = (df['INDIGENA'] == 1).mean()
kpi_resultados['Tasa de población indígena'] = tasa_indigena * 100

# Tasa de diabetes
tasa_diabetes = (df['DIABETES'] == 1).mean()
kpi_resultados['Tasa de diabetes'] = tasa_diabetes * 100

# Tasa de EPOC
tasa_epoc = (df['EPOC'] == 1).mean()
kpi_resultados['Tasa de EPOC'] = tasa_epoc * 100

# Tasa de asma
tasa_asma = (df['ASMA'] == 1).mean()
kpi_resultados['Tasa de asma'] = tasa_asma * 100

# Tasa de inmunosupresión
tasa_inmunosupresion = (df['INMUSUPR'] == 1).mean()
kpi_resultados['Tasa de inmunosupresión'] = tasa_inmunosupresion * 100

# Crear un gráfico de barras para visualizar los KPIs
plt.figure(figsize=(10, 6))
plt.barh(list(kpi_resultados.keys()), list(kpi_resultados.values()), color='skyblue')
plt.xlabel('Porcentaje (%)')
plt.title('KPIs de interés')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar los KPIs más importantes arriba
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Mostrar los valores en las barras
for i, v in enumerate(list(kpi_resultados.values())):
    plt.text(v + 1, i, f'{v:.2f}%', va='center', fontsize=10, color='black', fontweight='bold')

plt.show()
