import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Funciones.
def agregar_evento():
    fecha = entry_fecha.get_date()  # Obtener fecha del DateEntry
    hora = entry_hora.get()         # Obtener hora del Spinbox
    minuto = entry_minuto.get()     # Obtener minuto del Spinbox
    descripcion = entry_descripcion.get()

    if fecha and hora and minuto and descripcion:
        # Insertar los valores en el Treeview
        tree.insert("", "end", values=(fecha, f"{hora}:{minuto}", descripcion))
        # Limpiar las entradas después de agregar el evento
        entry_fecha.delete(0, tk.END)
        entry_hora.set("00")  # Resetear hora al valor por defecto
        entry_minuto.set("00")  # Resetear minuto al valor por defecto
        entry_descripcion.delete(0, tk.END)
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Evento agregado correctamente.")
    else:
        # Mostrar mensaje si falta información
        messagebox.showwarning("Faltan datos", "Por favor, completa todos los campos.")

def eliminar_evento():
    selected_item = tree.selection()  # Obtener el item seleccionado
    if selected_item:
        tree.delete(selected_item)  # Eliminar el evento seleccionado
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Evento eliminado correctamente.")
    else:
        messagebox.showwarning("Selección inválida", "Por favor, selecciona un evento para eliminar.")

# Función que se ejecutará al presionar el botón "Salir"
def salir():
    root.quit()

# Ventana principal.
root = tk.Tk()
root.title("Agenda de Eventos")
root.geometry("700x600")

# Crear lista Treeview.
tree = ttk.Treeview(root, columns=("FECHA", "HORA", "DESCRIPCION"), show="headings")
tree.heading("FECHA", text="FECHA")
tree.heading("HORA", text="HORA")
tree.heading("DESCRIPCION", text="DESCRIPCION")

tree.pack(pady=20, fill="both", expand=True)

# Crear campos de entrada (Entry).
# Creación de "frame".
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

# Identificadores y cuadros de texto (labels, DateEntry y Spinbox).
tk.Label(frame_entry, text="Fecha").grid(row=0, column=0)
entry_fecha = DateEntry(frame_entry, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entry, text="Hora").grid(row=1, column=0)

# Spinbox para la hora: (hora)
entry_hora = ttk.Spinbox(frame_entry, from_=0, to=23, width=5, format="%02.0f", state="normal")
entry_hora.grid(row=1, column=1)
entry_hora.set("00")  # Valor por defecto

tk.Label(frame_entry, text="Minutos").grid(row=1, column=2)

# Spinbox para los minutos: (minutos)
entry_minuto = ttk.Spinbox(frame_entry, from_=0, to=59, width=5, format="%02.0f", state="normal")
entry_minuto.grid(row=1, column=3)
entry_minuto.set("00")  # Valor por defecto

tk.Label(frame_entry, text="Descripcion").grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_entry)
entry_descripcion.grid(row=2, column=1)

# Botón agregar.
frame_Button = tk.Frame(root)
frame_Button.pack(pady=10)
btn_agregar = tk.Button(frame_Button, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

# Botón eliminar
btn_eliminar = tk.Button(frame_Button, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

# Crear el botón "Salir"
boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.pack()

# Iniciar ventana principal.
root.mainloop()