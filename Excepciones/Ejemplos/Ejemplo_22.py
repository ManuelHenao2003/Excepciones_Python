# Intenta ejecutar el código dentro del bloque try
try:

    # Solicita al usuario que introduzca un número
    numero = int(input("Introduce un número: "))

    # Divide 100 entre el número ingresado
    resultado = 100 / numero

# Se ejecuta si el usuario ingresa un valor que no es numérico
except ValueError:

    # Muestra un mensaje indicando que debe ingresar un número válido
    print("Debes introducir un número válido.")

# Se ejecuta si el usuario ingresa 0
except ZeroDivisionError:

    # Muestra un mensaje indicando que no se puede dividir entre cero
    print("No puedes dividir entre cero.")

# Se ejecuta únicamente si no ocurrió ninguna excepción
else:

    # Muestra el resultado de la división
    print(f"El resultado es:{resultado}")

    # Este código solo se ejecuta si no hubo excepciones