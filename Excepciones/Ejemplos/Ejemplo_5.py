# Función para pedir y validar la edad del usuario
def obtener_edad():

    # Bucle que se repetirá hasta que el usuario ingrese un dato válido
    while True:
        try:
            # Solicita al usuario que ingrese su edad
            edad = int(input("¿Cuál es tu edad? "))

            # Verifica si la edad es negativa
            if edad < 0:
                print("La edad no puede ser negativa.")

                # Vuelve a pedir el dato
                continue

            # Retorna la edad si es válida
            return edad

        except ValueError:
            # Se ejecuta si el usuario escribe texto
            # u otro valor que no sea un número entero
            print("Por favor, introduce un número entero.")

# Llama a la función y guarda el valor retornado
edad_usuario = obtener_edad()

# Muestra la edad ingresada por el usuario
print(f"Tu edad es: {edad_usuario}")