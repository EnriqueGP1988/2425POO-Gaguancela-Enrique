# Clase Libro que indica un libro disponible en la biblioteca.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para el título y autor para que no existan repeticiones.
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario para las personas que van hacer uso de los libros.
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario  # ID único del usuario.
        self.nombre = nombre
        self.libros_prestados = []  # Lista para almacenar los libros prestados al usuario.

    def __str__(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}"


# Clase Biblioteca para gestionar lps libro, usuarios y préstamos.
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor.
        self.usuarios = set()  # Conjunto para asegurar IDs de usuario únicos.
        self.historial_prestamos = {}  # Diccionario para registrar los préstamos.

    # Añadir libros a la biblioteca.
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    # Quitar un libro de la biblioteca.
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no se encuentra en la biblioteca.")

    # Registrar nuevo usuario.
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in [u.id_usuario for u in self.usuarios]:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios.add(usuario)
            print(f"Usuario registrado: {usuario}")

    # Dar de baja a un usuario.
    def dar_de_baja_usuario(self, id_usuario):
        usuario_a_borrar = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_a_borrar = usuario
                break
        if usuario_a_borrar:
            self.usuarios.remove(usuario_a_borrar)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El usuario con ID {id_usuario} no se encuentra registrado.")

    # Préstamo de  un libro.
    def prestar_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)

        if usuario and libro:
            if isbn in self.libros:
                self.libros.pop(isbn)
                usuario.libros_prestados.append(libro)
                print(f"Libro prestado: {libro} a {usuario}")
                if id_usuario not in self.historial_prestamos:
                    self.historial_prestamos[id_usuario] = []
                self.historial_prestamos[id_usuario].append(libro)
            else:
                print(f"El libro con ISBN {isbn} no se encuentra disponible en la biblioteca.")
        else:
            print("Usuario o libro no encontrados.")

    # Devolución del libro prestado.
    def devolver_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)

        if usuario and libro:
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro devuelto: {libro} por {usuario}")
            else:
                print(f"El libro con ISBN {isbn} no está prestado a {usuario}.")
        else:
            print("Usuario o libro no encontrados.")

    # Buscar libro por ISBN
    def buscar_libro(self, isbn):
        return self.libros.get(isbn, None)

    # Buscar usuario por ID.
    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    # Listar todos los libros prestados a un mismo usuario.
    def listar_libros_prestados(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"No existen libros prestados a {usuario}.")
        else:
            print("Usuario no encontrado.")

    # Mostrar todos los libros disponibles en la biblioteca.
    def listar_libros_disponibles(self):
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros.values():
                print(libro)
        else:
            print("No hay libros disponibles en la biblioteca.")


# Menú de opciones.
def mostrar_menu():
    print("\n*** Menú de Gestión de Biblioteca ***")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro por ISBN")
    print("8. Listar libros prestados")
    print("9. Listar libros disponibles")
    print("10. Salir")


# Función para ejecutar las opciones del menú
def ejecutar_menu():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-10): ")

        if opcion == "1":
            # Añadir libro
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            # Eliminar libro.
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Registrar usuario.
            id_usuario = int(input("ID de usuario (único): "))
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            # Dar de baja usuario.
            id_usuario = int(input("Ingrese el ID de usuario a dar de baja: "))
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "5":
            # Prestamo de libro.
            id_usuario = int(input("ID del usuario que solicita el libro: "))
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            # Devolver libro.
            id_usuario = int(input("ID del usuario que devuelve el libro: "))
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            # Búsqueda de  libro por ISBN.
            isbn = input("Ingrese el ISBN del libro a buscar: ")
            libro = biblioteca.buscar_libro(isbn)
            if libro:
                print(libro)
            else:
                print("Libro no encontrado.")

        elif opcion == "8":
            # Listar libros prestados.
            id_usuario = int(input("ID del usuario para listar libros prestados: "))
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            # Listar libros disponibles.
            biblioteca.listar_libros_disponibles()

        elif opcion == "10":
            # Salir
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válidad.")


# Ejecución del sistema.
if __name__ == "__main__":
    ejecutar_menu()
