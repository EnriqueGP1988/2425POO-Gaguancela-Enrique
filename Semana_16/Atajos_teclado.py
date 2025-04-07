import tkinter as tk
from tkinter import messagebox


# Función para añadir tarea.
def add_task():
    task = entry.get()

    # Verificar si la tarea contiene la letra 'D' o 'd'. Si contiene "D", no hacer nada y no mostrar ningún mensaje.
    if 'D' in task or 'd' in task:
        entry.delete(0, tk.END)  # Borra el texto en el Entry para que se pueda intentar de nuevo.
        return  # No hace nada si contiene "D" o "d".

    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea.")


# Función para marcar tarea como completada.
def mark_completed(event=None):
    try:
        selected_task_index = listbox.curselection()[0]  # Obtiene la tarea seleccionada.
        task = listbox.get(selected_task_index)
        # Añadir la palabra "Completada" al final de la tarea
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, f"{task} [*** Tarea Completada ***]")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para completarla")


# Función para eliminar tarea.
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)

        # Confirmar si el usuario quiere eliminar la tarea.
        confirm = messagebox.askyesno("Confirmación de Eliminación",
                                      f"¿Está seguro de que desea eliminar la tarea: '{task}'?")

        if confirm:  # Si el usuario confirma la eliminación.
            listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")


# Función para marcar tarea como completada con doble clic.
def mark_task_on_double_click(event):
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        # Añadir la palabra "Completada" al final de la tarea
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, f"{task} [*** Tarea Completada ***]")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para completarla")


# Función para confirmar el cierre de la aplicación.
def confirm_exit(event=None):
    # Mostrar un cuadro de diálogo para confirmar si desea salir
    answer = messagebox.askyesno("Confirmar Salida", "¿Está seguro de que desea salir?")
    if answer:  # Si la respuesta es 'Sí'
        root.quit()


# Crear ventana principal.
root = tk.Tk()
root.title("Gestión de Tareas con GUI")

# Configurar interfaz gráfica.
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(frame, text="Añadir Tarea", width=20, command=add_task)
add_button.grid(row=0, column=1, padx=10)

# Lista de tareas.
listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Botones de control.
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

mark_button = tk.Button(control_frame, text="Completar Tarea", width=20, command=mark_completed)
mark_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(control_frame, text="Eliminar Tarea", width=20, command=delete_task)
delete_button.grid(row=0, column=1, padx=10)

# Botón de Salida
exit_button = tk.Button(root, text="Salir", width=20, command=confirm_exit)
exit_button.pack(pady=10)

# Asignar atajos de teclado
root.bind("<Return>", lambda event: add_task())  # Tecla Enter para añadir tarea.
root.bind("<Delete>", lambda event: delete_task())  # Tecla Delete para eliminar tarea.
root.bind("<d>", lambda event: delete_task())  # Tecla D para eliminar tarea.
root.bind("<Escape>", confirm_exit)  # Tecla Escape para confirmar salida.


# Asignar tecla "C" para marcar tarea como completada solo si hay una tarea seleccionada.
def on_c_key_press(event):
    if listbox.curselection():  # Verifica si hay una tarea seleccionada.
        mark_completed(event)


root.bind("<c>", on_c_key_press)  # Tecla C para marcar como completada solo si hay tarea seleccionada.

# Asignar doble clic para marcar tarea como completada.
listbox.bind("<Double-1>", mark_task_on_double_click)


# Función para evitar que las teclas de eliminar funcionen si el Entry tiene el foco
def on_key_press(event):
    if event.keysym in ["d", "Delete"]:
        if entry.focus_get():  # Si el foco está en el Entry, no hacer nada.
            return "break"  # Esto evitará que se ejecute la acción de eliminar.


# Vincular la función de bloqueo para las teclas "D" y "Delete" mientras el Entry tiene el foco.
root.bind("<KeyPress>", on_key_press)

# Iniciar la aplicación.
root.mainloop()
