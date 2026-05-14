# Intenta ejecutar el código dentro del bloque try
try:

    # Crea una lista con tres elementos
    lista = [1, 2, 3]

    # Intenta acceder a la posición 10 de la lista
    elemento = lista[10]

# Se ejecuta si el índice no existe en la lista
except IndexError:

    # Muestra un mensaje indicando que el índice está fuera del rango
    print("El índice está fuera del rango de la lista")