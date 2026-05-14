# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta sumar un texto ("42") con un número entero (10)
    resultado = "42" + 10

# Se ejecuta si se intentan operar tipos de datos incompatibles
except TypeError:

    # Muestra un mensaje indicando que no se pueden sumar tipos diferentes
    print("No se pueden sumar tipos diferentes")