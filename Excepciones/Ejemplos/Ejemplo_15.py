# Intenta ejecutar el código dentro del bloque try
try:

    # Guarda el texto "Hola" en la variable texto
    texto = "Hola"

    # Intenta acceder al atributo "size" del string
    # pero los strings no tienen ese atributo
    longitud = texto.size

# Se ejecuta si el objeto no tiene el atributo solicitado
except AttributeError:

    # Muestra un mensaje indicando que el atributo no existe
    print("El objeto string no tiene el atributo 'size'")