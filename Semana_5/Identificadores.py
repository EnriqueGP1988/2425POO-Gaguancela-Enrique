# EJERCICIO #1

# Verificar si un número es positivo o negativo.

numero = float(input("Ingrese el número a verificar: "))

# Verificar si el número es positivo, negativo o cero
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print(f"El número es cero.")



#EJERCICIO #2

# Realizar el ejercicio anterior utilizando funciones

# Definir la función.
def verificar_numero(numero):
    if numero > 0:
        return f"El número {numero} es positivo."
    elif numero < 0:
        return f"El número {numero} es negativo."
    else:
        return "El número es cero."

# Solicitar al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Llamar a la función e imprimir el resultado
resultado = verificar_numero(numero)
print(resultado)
