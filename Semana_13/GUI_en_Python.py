import tkinter as tk
from tkinter import messagebox

# Función para agregar información.
def agregar_dato():
    # Obtener la información ingresada.
    dato = entrada_texto.get()
    # Alerta en caso que el campo para ingresar información
    # Se encuentre vacío.
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Alerta", "Por favor ingrese información.")

# Función para limpiar la lista.
def limpiar_lista():
    # Borrar los datos que se encuentra en la lista.
    lista_datos.delete(0, tk.END)

# Ventana principal.
ventana = tk.Tk()
# Título de la ventana.
ventana.title("POO: GUIE en Python")
# Dimensiones de la ventana: ancho x alto.
ventana.geometry("400x500")


# Crear un marco para organizar los elementos
marco = tk.Frame(ventana)
marco.pack(padx=10, pady=10)

# Etiqueta.
etiqueta = tk.Label(marco, text="Ingrese la información:")
etiqueta.grid(row=0, column=0, padx=5, pady=5)

# Campo de texto para ingresar la información.
entrada_texto = tk.Entry(marco, width=30)
entrada_texto.grid(row=0, column=1, padx=5, pady=5)

# Botón "Agregar"
boton_agregar = tk.Button(marco, text="Agregar", command=agregar_dato)
boton_agregar.grid(row=1, column=0, columnspan=2, pady=5)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(marco, width=40, height=10)
lista_datos.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Botón "Limpiar"
boton_limpiar = tk.Button(marco, text="Limpiar", command=limpiar_lista)
boton_limpiar.grid(row=3, column=0, columnspan=2, pady=5)

# Ejecutar la ventana
ventana.mainloop()
