# COMPARACIÓN DE PROGRAMACIÓN TRADICIONAL Y POO

# POO
# Implementación de un programa para determinar el promedio semanal del clima.

class TemperaturasSemana:
    def __init__(self):

        # Iniciar las temperaturas vacía
        self.temperaturas = []

    # Ingreso diario de temperaturas.
    def ingresar_temperaturas(self):
        # Rango correspondiente a los 7 días de la semana
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura correspondiente al día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("El valor ingresado es incorrecto.")

    # Calcular el promedio semanal.
    def calcular_promedio(self):
        if len(self.temperaturas) == 7:
            promedio = sum(self.temperaturas) / len(self.temperaturas)
            return promedio
        else:
            return None

    # Impresión del resultado final.
    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        if promedio is not None:
            print(f"\nEl promedio de temperatura de la semana es de: {promedio:.2f}°C")
        else:
            print("No se han ingresado las temperaturas correctamente.")


# Función principal
def main():
    print("Bienvenido al sistema")

    # Crear una instancia de la clase TemperaturasSemana
    semana = TemperaturasSemana()

    # Ingresar las temperaturas
    semana.ingresar_temperaturas()

    # Mostrar el resultado
    semana.mostrar_resultado()


if __name__ == "__main__":
    main()
