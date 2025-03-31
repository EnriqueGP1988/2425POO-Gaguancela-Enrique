import tkinter as tk
from tkinter import messagebox

# Función para agregar nueva tarea.
def agregar_tarea():
    tarea = entrada_tarea.get()  # Obtener la tarea desde el Entry.
    if tarea != "":  # Verificar que el campo no se encuentre vacío.
        lista_tareas.insert(tk.END, tarea)  # Agregar la tarea al Listbox.
        entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada.
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea.")

# Función para marcar una tarea como completada.
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()  # Obtener tarea seleccionada
        if not tarea_seleccionada:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")
            return
        tarea = lista_tareas.get(tarea_seleccionada)  # Obtener el texto de la tarea seleccionada.
        # Marcar tarea como completada.
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, tarea + "  (*** Completada ***)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()  # Obtener tarea seleccionada.
        lista_tareas.delete(tarea_seleccionada)  # Eliminar la tarea seleccionada.
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea.")

# Función para manejar la tecla Enter para agregar tareas
def presionar_enter(event):
    agregar_tarea()

# Función para salir del sistema.
def salir_del_sistema():
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir del sistema?")
    if respuesta:  # Si el usuario confirma que quiere salir.
        root.quit()  # Cerrar la ventana.

# Función para manejar la tecla Escape
def on_escape_pressed(event):
    respuesta = messagebox.askyesno("¡ ATENCIÓN !", "¿Estás seguro de que quieres salir del sistema?")
    if respuesta:  # Si el usuario confirma.
        root.quit()  # Cerrar la ventana.
    # Si el usuario elige cancelar, no hace nada.

# Ventana principal.
root = tk.Tk()
root.title("APLICACIÓN GUI")
root.geometry("400x600")

# Crear un campo de entrada (Entry) para escribir las tareas.
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", presionar_enter)  # Asociar la tecla Enter con la función.

# Crear un Listbox para mostrar las tareas ingresadas.
lista_tareas = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Evento de doble clic para marcar una tarea como completada.
lista_tareas.bind("<Double-1>", lambda event: marcar_completada())

# Crear los botones para las acciones
boton_agregar = tk.Button(root, text="Añadir Tarea", width=20, command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(root, text="Completar Tarea", width=20, command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Crear el botón para salir del sistema.
boton_salir = tk.Button(root, text="Salir del Sistema", width=20, command=salir_del_sistema)
boton_salir.pack(pady=20)

# Vincular evento de tecla Escape a la ventana principal.
root.bind('<Escape>', on_escape_pressed)

# Ejecutar el sistema.
root.mainloop()
