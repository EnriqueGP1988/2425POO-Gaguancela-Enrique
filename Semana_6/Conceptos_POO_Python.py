# Clase base (padre)
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado (encapsulación)
        self.__edad = edad      # Atributo privado (encapsulación)

    # Métodos getters para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método común para todos los animales
    def hacer_sonido(self):
        print("El animal hace un sonido.")

# Clase derivada (hija) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.raza = raza

    # Sobrescritura del método de la clase base (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Guau!")

    # Método para mostrar información del perro
    def mostrar_informacion(self):
        print(f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()} años, Raza: {self.raza}")


# Otra clase derivada (hija) que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescritura del método de la clase base (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Miau!")

    # Método para mostrar información del gato
    def mostrar_informacion(self):
        print(f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()} años, Color: {self.color}")


# Función que demuestra polimorfismo con argumentos
def hacer_sonido_de_animal(animal: Animal):
    animal.hacer_sonido()

# Crear instancias de las clases
perro = Perro("Rex", 5, "Pastor Alemán")
gato = Gato("Felix", 3, "Negro")

# Mostrar información de los animales
perro.mostrar_informacion()
gato.mostrar_informacion()

# Demostración de polimorfismo
hacer_sonido_de_animal(perro)  # El perro hace un sonido
hacer_sonido_de_animal(gato)   # El gato hace un sonido
