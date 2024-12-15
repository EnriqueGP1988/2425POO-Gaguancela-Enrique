# Tarea de POO en la cual mediante una clase principal
# llamada VEHICULOS se la puede utilizar para crear dos
# objetos llamados COCHE y MOTO

# ENCAPSULAMIENTO
# Creación de la clase llamada "vehiculo".
class vehiculo:
    def __init__(self, marca, modelo, año):
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    # Métodos getter y setter
    # Getters permiten acceder a los atributos de una clase de manera controlada, sin exponer directamente los datos.
    # Setters permiten modificar atributos de manera controlada, con validación o transformaciones adicionales.
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_color(self, año):
        self.__año = año


# HERENCIA
class Coche(vehiculo):
    def __init__(self, marca, modelo, año, puertas):

        # Llamada al constructor principal "vehiculo"
        super().__init__(marca, modelo, año)
        # Se añade un nuevo atributo al "coche" el mismo que nos va a permitir dar a conocer el número de puertas
        self.__puertas = puertas

    # Implementación del método de la clase principal
    def mostrar_informacion(self):
        return f"Coche: {self.get_marca()} {self.get_modelo()}, Año: {self.get_año()}, Puertas: {self.__puertas}"

    # Impresión de lo que se va a realizar en el coche.
    def abrir_puerta(self):
        print(f"Abriendo las puertas del {self.get_marca()} {self.get_modelo()}.")

class Moto(vehiculo):
    def __init__(self, marca, modelo, año, cilindraje):
        super().__init__(marca, modelo, año)
        # Se añade un nuevo atributo a "moto" el cual nos permitirá ingresar el "cilindraje"
        self.__cilindraje = cilindraje

    def mostrar_informacion(self):
        return f"Moto: {self.get_marca()} {self.get_modelo()}, Año: {self.get_año()}, Cilindraje: {self.__cilindraje}cc"

    def arrancar_motor(self):
        # Impresión de lo que se va a realizar en la moto.
        print(f"Arrancando el motor de la moto {self.get_marca()} {self.get_modelo()}.")

# POLIMORFISMO
def mostrar_detalles_vehiculo(vehiculo):
    print(vehiculo.mostrar_informacion())

# Programa principal
if __name__ == "__main__":
    # Creación de los objetos
    coche = Coche("Chevrolet", "Groove", "2024", 4)
    moto = Moto("Yamaha", "Adventure", "2024", 500)

    # Información (polimorfismo).
    # Llamando a la información del coche
    mostrar_detalles_vehiculo(coche)
    # Llamando a la información de la moto.
    mostrar_detalles_vehiculo(moto)

    # Métodos específicos.
    coche.abrir_puerta()
    moto.arrancar_motor()
