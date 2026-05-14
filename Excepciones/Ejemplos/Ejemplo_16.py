# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta mostrar una variable que no ha sido creada
    print(variable_no_definida)

# Se ejecuta si la variable no existe o no está definida
except NameError:

    # Muestra un mensaje indicando que la variable no está definida
    print("La variable no está definida")