# Creación de la clase "Producto" en la cual se definen los parámetros a utilizar.
# Contiene los atributos como: ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

# Def para definir una función, indica el inicio de una función y la forma en que se declara.
# Además de métodos para obtener y establecer esos atributos.
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"



import pickle  # Para la serialización y deserialización de los datos

# Creación de la clase "Inventario"
# utiliza un diccionario para almacenar los productos, con el ID del producto como clave.
# Implementa los métodos para añadir, eliminar, actualizar productos, buscar producto, mostrar productos,
# Guardar y cargar inventario.
class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.obtener_id() not in self.productos:
            self.productos[producto.obtener_id()] = producto
        else:
            print(f"El producto con ID {producto.obtener_id()} ya existe.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)
        print("Inventario guardado exitosamente.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe. Creando un inventario vacío.")


# Creación de las diferentes opciones o tareas a realizar dentro del inventario.
def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Guardar Inventario")
    print("7. Cargar Inventario")
    print("8. Salir")

def ejecutar():
    inventario = Inventario()
    archivo_inventario = "inventario.dat"

# Interacción con las distintas opciones disponibles del inventario a mostrar.
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            inventario.guardar_inventario(archivo_inventario)

        elif opcion == "7":
            inventario.cargar_inventario(archivo_inventario)

        elif opcion == "8":
            print("¡Gracias por utilizar el sistema!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    ejecutar()
