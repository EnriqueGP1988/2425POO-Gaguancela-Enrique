import os

# Creación de la clase "Producto".
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

# Creación de la clase "Inventario".
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    # Cargar inventario desde archivo
    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as file:
                    for line in file:
                        try:
                            id, nombre, cantidad, precio = line.strip().split(",")
                            producto = Producto(int(id), nombre, int(cantidad), float(precio))
                            self.productos.append(producto)
                        except ValueError:
                            print(f"Error al leer la línea: {line}. Formato incorrecto.")
            except FileNotFoundError:
                print("El archivo no fue encontrado. Se creará uno nuevo.")
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            print("El archivo de inventario no existe. Se creará uno nuevo.")

    # Guardar inventario en archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error de permisos al intentar guardar el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    # Añadir producto al inventario
    def añadir_producto(self, id, nombre, cantidad, precio):
        for producto in self.productos:
            if producto.get_id() == id:
                print("Error: El ID ya existe.")
                return
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_inventario()
        print("Producto añadido exitosamente.")

    # Eliminar producto
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    # Actualizar cantidad o precio
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            print("Producto encontrado:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if self.productos:
            print("Productos en inventario:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

# Menú de las opciones disponibles en el sistema.
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese ID del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.añadir_producto(id, nombre, cantidad, precio)

        elif opcion == "2":
            id = int(input("Ingrese ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no modificar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no modificar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("*** Gracias por utilizar el sistema ***")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú del sistema.
menu()
