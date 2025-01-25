# Creación de la clase "USUARIO"
class Usuario:
    def __init__(self, nombre, edad):
        # Constructor que inicializa el nombre y la edad del usuario.
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado al usuario: {self.nombre}, {self.edad} años.")

    def __del__(self):
        # Destructor que se llama cuando el objeto es destruido o eliminado.
        print(f"El usuario {self.nombre} ha sido eliminada.")


# Creación del objeto de la clase Persona
persona = Usuario("Enrique", 36)

# Eliminar el objeto.
del persona