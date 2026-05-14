# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta dividir 5 entre 0
    resultado = 5 / 0

# Se ejecuta si ocurre un error de división entre cero
except ZeroDivisionError:

    # Muestra un mensaje indicando que no se puede dividir entre cero
    print("No es posible dividir entre cero")