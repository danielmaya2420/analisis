import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Ruta del archivo Excel
archivo_excel = 'DB.xlsx'

# Función para crear un nuevo registro
def crear_registro():
    global df  # Declarar df como global
    genero = genero_var.get()
    edad = edad_var.get()
    diabetes = diabetes_var.get()
    obesidad = obesidad_var.get()
    tabaquismo = tabaquismo_var.get()
    hipertenso = hipertenso_var.get()

    nuevo_registro = pd.DataFrame({
        'ID': [len(df) + 1],
        'GENERO': [genero],
        'EDAD': [edad],
        'DIABETES': [diabetes],
        'OBESIDAD': [obesidad],
        'TABAQUISMO': [tabaquismo],
        'HIPERTENSO': [hipertenso]
    })

    df = pd.concat([df, nuevo_registro], ignore_index=True)

    df.to_excel(archivo_excel, index=False)
    messagebox.showinfo("Éxito", "Registro creado exitosamente.")
    mostrar_registros()  # Actualizar la tabla después de agregar un registro

# Función para mostrar todos los registros
def mostrar_registros():
    global df  # Declarar df como global

    # Limpiar la tabla existente
    for row in tabla.get_children():
        tabla.delete(row)

    # Mostrar los registros en la tabla
    for index, row in df.iterrows():
        tabla.insert("", "end", values=row.tolist())

# Función para editar un registro
def editar_registro(event):
    item = tabla.selection()[0]  # Obtener el elemento seleccionado
    if item:
        # Obtener los valores de la fila seleccionada
        valores = tabla.item(item, 'values')
        # Llenar los campos de entrada con los valores actuales
        genero_var.set(valores[1])
        edad_var.set(valores[2])
        diabetes_var.set(valores[3])
        obesidad_var.set(valores[4])
        tabaquismo_var.set(valores[5])
        hipertenso_var.set(valores[6])
        # Mostrar ventana de edición
        ventana_edicion()

# Función para guardar la edición de un registro
def guardar_edicion():
    global df  # Declarar df como global
    item = tabla.selection()[0]  # Obtener el elemento seleccionado
    if item:
        # Obtener los valores de la fila seleccionada
        valores = tabla.item(item, 'values')
        # Obtener el índice de la fila en el DataFrame
        index = df[df['ID'] == int(valores[0])].index[0]
        # Actualizar los valores en el DataFrame
        df.at[index, 'GENERO'] = genero_var.get()
        df.at[index, 'EDAD'] = edad_var.get()
        df.at[index, 'DIABETES'] = diabetes_var.get()
        df.at[index, 'OBESIDAD'] = obesidad_var.get()
        df.at[index, 'TABAQUISMO'] = tabaquismo_var.get()
        df.at[index, 'HIPERTENSO'] = hipertenso_var.get()
        # Guardar el DataFrame actualizado en el archivo Excel
        df.to_excel(archivo_excel, index=False)
        messagebox.showinfo("Éxito", "Registro actualizado exitosamente.")
        ventana_edicion_actual.destroy()
        mostrar_registros()  # Actualizar la tabla después de editar un registro

# Función para mostrar la ventana de edición
def ventana_edicion():
    global ventana_edicion_actual
    ventana_edicion_actual = tk.Toplevel(root)
    ventana_edicion_actual.title("Editar Registro")

    # Crear etiquetas y campos de entrada en la ventana de edición
    etiqueta_genero_edicion = tk.Label(ventana_edicion_actual, text="Género (M/F):")
    entrada_genero_edicion = tk.Entry(ventana_edicion_actual, textvariable=genero_var)
    etiqueta_edad_edicion = tk.Label(ventana_edicion_actual, text="Edad:")
    entrada_edad_edicion = tk.Entry(ventana_edicion_actual, textvariable=edad_var)
    etiqueta_diabetes_edicion = tk.Label(ventana_edicion_actual, text="Diabetes (Sí/No):")
    entrada_diabetes_edicion = tk.Entry(ventana_edicion_actual, textvariable=diabetes_var)
    etiqueta_obesidad_edicion = tk.Label(ventana_edicion_actual, text="Obesidad (Sí/No):")
    entrada_obesidad_edicion = tk.Entry(ventana_edicion_actual, textvariable=obesidad_var)
    etiqueta_tabaquismo_edicion = tk.Label(ventana_edicion_actual, text="Tabaquismo (Sí/No):")
    entrada_tabaquismo_edicion = tk.Entry(ventana_edicion_actual, textvariable=tabaquismo_var)
    etiqueta_hipertenso_edicion = tk.Label(ventana_edicion_actual, text="Hipertensión (Sí/No):")
    entrada_hipertenso_edicion = tk.Entry(ventana_edicion_actual, textvariable=hipertenso_var)
    boton_guardar_edicion = tk.Button(ventana_edicion_actual, text="Guardar Edición", command=guardar_edicion)

    # Posicionar elementos en la ventana de edición
    etiqueta_genero_edicion.grid(row=0, column=0)
    entrada_genero_edicion.grid(row=0, column=1)
    etiqueta_edad_edicion.grid(row=1, column=0)
    entrada_edad_edicion.grid(row=1, column=1)
    etiqueta_diabetes_edicion.grid(row=2, column=0)
    entrada_diabetes_edicion.grid(row=2, column=1)
    etiqueta_obesidad_edicion.grid(row=3, column=0)
    entrada_obesidad_edicion.grid(row=3, column=1)
    etiqueta_tabaquismo_edicion.grid(row=4, column=0)
    entrada_tabaquismo_edicion.grid(row=4, column=1)
    etiqueta_hipertenso_edicion.grid(row=5, column=0)
    entrada_hipertenso_edicion.grid(row=5, column=1)
    boton_guardar_edicion.grid(row=6, column=0, columnspan=2)

# Función para eliminar un registro
def eliminar_registro():
    item = tabla.selection()[0]  # Obtener el elemento seleccionado
    if item:
        # Obtener los valores de la fila seleccionada
        valores = tabla.item(item, 'values')
        # Obtener el índice de la fila en el DataFrame
        index = df[df['ID'] == int(valores[0])].index[0]
        # Eliminar la fila del DataFrame
        df.drop(index, inplace=True)
        # Guardar el DataFrame actualizado en el archivo Excel
        df.to_excel(archivo_excel, index=False)
        messagebox.showinfo("Éxito", "Registro eliminado exitosamente.")
        mostrar_registros()  # Actualizar la tabla después de eliminar un registro

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación CRUD")

# Variables para almacenar la entrada del usuario
genero_var = tk.StringVar()
edad_var = tk.IntVar()
diabetes_var = tk.StringVar()
obesidad_var = tk.StringVar()
tabaquismo_var = tk.StringVar()
hipertenso_var = tk.StringVar()

# Crear etiquetas y campos de entrada
etiqueta_genero = tk.Label(root, text="Género (M/F):")
entrada_genero = tk.Entry(root, textvariable=genero_var)
etiqueta_edad = tk.Label(root, text="Edad:")
entrada_edad = tk.Entry(root, textvariable=edad_var)
etiqueta_diabetes = tk.Label(root, text="Diabetes (Sí/No):")
entrada_diabetes = tk.Entry(root, textvariable=diabetes_var)
etiqueta_obesidad = tk.Label(root, text="Obesidad (Sí/No):")
entrada_obesidad = tk.Entry(root, textvariable=obesidad_var)
etiqueta_tabaquismo = tk.Label(root, text="Tabaquismo (Sí/No):")
entrada_tabaquismo = tk.Entry(root, textvariable=tabaquismo_var)
etiqueta_hipertenso = tk.Label(root, text="Hipertensión (Sí/No):")
entrada_hipertenso = tk.Entry(root, textvariable=hipertenso_var)

# Crear botones
boton_crear = tk.Button(root, text="Crear registro", command=crear_registro)
boton_mostrar = tk.Button(root, text="Mostrar registros", command=mostrar_registros)

# Crear botón para eliminar registro
boton_eliminar = tk.Button(root, text="Eliminar registro", command=eliminar_registro)

# Posicionar elementos en la ventana
etiqueta_genero.grid(row=0, column=0)
entrada_genero.grid(row=0, column=1)
etiqueta_edad.grid(row=1, column=0)
entrada_edad.grid(row=1, column=1)
etiqueta_diabetes.grid(row=2, column=0)
entrada_diabetes.grid(row=2, column=1)
etiqueta_obesidad.grid(row=3, column=0)
entrada_obesidad.grid(row=3, column=1)
etiqueta_tabaquismo.grid(row=4, column=0)
entrada_tabaquismo.grid(row=4, column=1)
etiqueta_hipertenso.grid(row=5, column=0)
entrada_hipertenso.grid(row=5, column=1)

boton_crear.grid(row=6, column=0, columnspan=2)
boton_mostrar.grid(row=7, column=0, columnspan=2)
boton_eliminar.grid(row=8, column=0, columnspan=2)

# Crear tabla para mostrar registros
columnas = ['ID', 'GENERO', 'EDAD', 'DIABETES', 'OBESIDAD', 'TABAQUISMO', 'HIPERTENSO']
tabla = ttk.Treeview(root, columns=columnas, show='headings')

# Configurar encabezados de columna
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=80)

tabla.grid(row=9, column=0, columnspan=2)

# Enlazar evento de doble clic en la tabla para editar registros
tabla.bind("<Double-1>", editar_registro)

# Función principal
def main():
    global df
    try:
        df = pd.read_excel(archivo_excel)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['ID', 'GENERO', 'EDAD', 'DIABETES', 'OBESIDAD', 'TABAQUISMO', 'HIPERTENSO'])

    root.mainloop()

if __name__ == "__main__":
    main()
