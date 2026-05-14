# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta calcular 10 elevado a 1,000,000
    # El resultado es demasiado grande
    resultado = 10.0 ** 1000000

# Se ejecuta si el número es demasiado grande para manejarse
except OverflowError:

    # Muestra un mensaje indicando que el número es muy grande
    print("El número es demasiado grande para ser representado")