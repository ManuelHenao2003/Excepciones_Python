try:
    # Solicita al usuario que ingrese un número
    numero = int(input("Introduce un número: "))

    # Divide 100 entre el número ingresado
    resultado = 100 / numero

    # Muestra el resultado de la división
    print(f"100 dividido por {numero} es {resultado}")

except ZeroDivisionError:
    # Se ejecuta si el usuario ingresa 0
    # porque no se puede dividir entre cero
    print("No puedes dividir entre cero.")

except ValueError:
    # Se ejecuta si el usuario ingresa texto
    # u otro valor que no sea un número válido
    print("Debes introducir un número válido.")