# Intenta ejecutar el código dentro del bloque try
try:

    # Intenta convertir el texto "abc" en un número entero
    numero = int("abc")

# Se ejecuta si el valor no puede convertirse a entero
except ValueError:

    # Muestra un mensaje indicando que la cadena no es un número válido
    print("La cadena no representa un número válido")