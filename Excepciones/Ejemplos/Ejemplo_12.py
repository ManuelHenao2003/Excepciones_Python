# Intenta ejecutar el código dentro del bloque try
try:

    # Crea un diccionario con las claves "nombre" y "edad"
    diccionario = {"nombre": "Ana", "edad": 25}

    # Intenta acceder a la clave "telefono"
    valor = diccionario["telefono"]

# Se ejecuta si la clave no existe en el diccionario
except KeyError:

    # Muestra un mensaje indicando que la clave no existe
    print("La clave 'telefono' no existe en el diccionario")