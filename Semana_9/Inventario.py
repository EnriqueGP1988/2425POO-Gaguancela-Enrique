# Creación de la clase "Producto".
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters que se utiliza para acceder a los valores de los atributos privados o protegidos de una clase.
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters se utiliza para modificar los valores de los atributos privados de una clase.
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Creación de la clase "Inventario".
class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir productos.
    def añadir_producto(self, id, nombre, cantidad, precio):
        # Comprobar si el ID de los productos existe.
        for producto in self.productos:
            if producto.get_id() == id:
                print("Error: El ID ya existe.")
                return
        # Crear un nuevo producto y añadirlo al inventario.
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido exitosamente.")

    # Eliminar producto.
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    # Actualizar cantidad o precio.
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    # Buscar producto por nombre.
    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            print("Producto encontrado:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos.
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
