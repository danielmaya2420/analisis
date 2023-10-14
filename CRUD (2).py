import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Ruta del archivo Excel
archivo_excel = 'DB.xlsx'

# Función para crear un nuevo registro
def crear_registro():
    global df
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
    mostrar_registros()

# Función para mostrar todos los registros
def mostrar_registros():
    global df
    for row in tabla.get_children():
        tabla.delete(row)

    for index, row in df.iterrows():
        tabla.insert("", "end", values=row.tolist())

# Función para editar un registro
def editar_registro(event):
    item = tabla.selection()[0]
    if item:
        valores = tabla.item(item, 'values')
        genero_var.set(valores[1])
        edad_var.set(valores[2])
        diabetes_var.set(valores[3])
        obesidad_var.set(valores[4])
        tabaquismo_var.set(valores[5])
        hipertenso_var.set(valores[6])
        ventana_edicion()

# Función para guardar la edición de un registro
def guardar_edicion():
    global df
    item = tabla.selection()[0]
    if item:
        valores = tabla.item(item, 'values')
        index = df[df['ID'] == int(valores[0])].index[0]
        df.at[index, 'GENERO'] = genero_var.get()
        df.at[index, 'EDAD'] = edad_var.get()
        df.at[index, 'DIABETES'] = diabetes_var.get()
        df.at[index, 'OBESIDAD'] = obesidad_var.get()
        df.at[index, 'TABAQUISMO'] = tabaquismo_var.get()
        df.at[index, 'HIPERTENSO'] = hipertenso_var.get()
        df.to_excel(archivo_excel, index=False)

        messagebox.showinfo("Éxito", "Registro actualizado exitosamente.")
        ventana_edicion_actual.destroy()
        mostrar_registros()

# Función para mostrar la ventana de edición
def ventana_edicion():
    global ventana_edicion_actual
    ventana_edicion_actual = tk.Toplevel(root)
    ventana_edicion_actual.title("Editar Registro")
    etiquetas = ["Género (M/F):", "Edad:", "Diabetes (Sí/No):", "Obesidad (Sí/No):", "Tabaquismo (Sí/No):", "Hipertensión (Sí/No):"]
    entradas = [genero_var, edad_var, diabetes_var, obesidad_var, tabaquismo_var, hipertenso_var]

    for i in range(len(etiquetas)):
        etiqueta = tk.Label(ventana_edicion_actual, text=etiquetas[i])
        etiqueta.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        entrada = tk.Entry(ventana_edicion_actual, textvariable=entradas[i])
        entrada.grid(row=i, column=1, padx=10, pady=5)

    boton_guardar_edicion = tk.Button(ventana_edicion_actual, text="Guardar Edición", command=guardar_edicion)
    boton_guardar_edicion.grid(row=len(etiquetas), column=0, columnspan=2, pady=10)

# Función para eliminar un registro
def eliminar_registro():
    item = tabla.selection()[0]
    if item:
        valores = tabla.item(item, 'values')
        index = df[df['ID'] == int(valores[0])].index[0]
        df.drop(index, inplace=True)
        df.to_excel(archivo_excel, index=False)

        messagebox.showinfo("Éxito", "Registro eliminado exitosamente.")
        mostrar_registros()

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
campos = [
    ("Género (M/F):", genero_var),
    ("Edad:", edad_var),
    ("Diabetes (Sí/No):", diabetes_var),
    ("Obesidad (Sí/No):", obesidad_var),
    ("Tabaquismo (Sí/No):", tabaquismo_var),
    ("Hipertensión (Sí/No):", hipertenso_var)
]

for i, (label_text, var) in enumerate(campos):
    etiqueta = tk.Label(root, text=label_text)
    etiqueta.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    entrada = tk.Entry(root, textvariable=var)
    entrada.grid(row=i, column=1, padx=10, pady=5)

# Crear botones
boton_crear = tk.Button(root, text="Crear registro", command=crear_registro)
boton_mostrar = tk.Button(root, text="Mostrar registros", command=mostrar_registros)
boton_eliminar = tk.Button(root, text="Eliminar registro", command=eliminar_registro)

# Posicionar elementos en la ventana
boton_crear.grid(row=len(campos), column=0, columnspan=2)
boton_mostrar.grid(row=len(campos) + 1, column=0, columnspan=2)
boton_eliminar.grid(row=len(campos) + 2, column=0, columnspan=2)

# Crear tabla para mostrar registros
columnas = ['ID', 'GENERO', 'EDAD', 'DIABETES', 'OBESIDAD', 'TABAQUISMO', 'HIPERTENSO']
tabla = ttk.Treeview(root, columns=columnas, show='headings')

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=80)

tabla.grid(row=len(campos) + 3, column=0, columnspan=2)

# Enlazar evento de doble clic en la tabla para editar registros
tabla.bind("<Double-1>", editar_registro)

# Función principal
