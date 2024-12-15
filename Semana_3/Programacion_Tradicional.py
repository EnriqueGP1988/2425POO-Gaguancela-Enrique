# COMPARACIÓN DE PROGRAMACIÓN TRADICIONAL Y POO

# PROGRAMACIÓN TRADICIONAL
# Implementación de un programa para determinar el promedio semanal del clima.

# Función para ingresar las temperaturas diarias de los 7 días de la semana.
def ingresar_temperaturas():
    temperaturas = []

    # Rango correspondiente a los 7 días de la semana
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura correspondiente al día {i + 1}: "))
                temperaturas.append(temp)
                # Función la cual nos permite controlar que el valor ingresado en temperatura
                # sea únicamente números.
                break
            except ValueError:
                print("El valor ingresado es incorrecto.")
    return temperaturas


# Función utilizada para calcular el promedio semanal de las temperaturas ingresadas.
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Función principal.
def main():
    print("Bienvenido al sistema")


    # Ingreso de las temperaturas.
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio semanal de las temperaturas
    promedio = calcular_promedio(temperaturas)

    # Impresión del resultado final.
    print(f"\nEl promedio de tempetatura de la semana es de: promedio:.2f}°C")


if __name__ == "__main__":
    main()