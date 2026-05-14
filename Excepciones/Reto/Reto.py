def dividir_numeros():

    try:
        # Solicitar al usuario que introduzca dos números
        numero1 = input("Introduce el primer número: ")
        numero2 = input("Introduce el segundo número: ")

        # Convertir las entradas a números enteros
        numero1 = int(numero1)
        numero2 = int(numero2)

        # Realizar la división del primer número entre el segundo
        resultado = numero1 / numero2

        # Devolver el resultado de la división
        print(f"El resultado es: {resultado}")

    except ValueError:
        # Se ejecuta si el usuario no introduce números válidos
        print("Debes introducir números enteros válidos.")

    except ZeroDivisionError:
        # Se ejecuta si el segundo número es 0
        print("No se puede dividir entre cero.")

    finally:
        # Se ejecuta siempre, ocurra o no un error
        print("Fin del programa.")


# Llamada a la función
dividir_numeros()